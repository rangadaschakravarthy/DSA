"""
Level 1: Hash Map Fundamentals & Fast Lookups

Topics Covered:
1. Two Sum (Unsorted Array) O(N)
2. First Unique Character in a String O(N)
3. Isomorphic Strings (Bi-directional Map Verification) O(N)

Complexity:
- Two Sum: O(N) time, O(N) space.
- First Unique Char: O(N) time, O(1) space (26 chars).
- Isomorphic Strings: O(N) time, O(1) space.
"""

from collections import Counter

def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Finds indices of two numbers in an unsorted array that add up to target.
    Uses Hash Map to store seen values: value -> index.
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def first_uniq_char(s: str) -> int:
    """
    Finds the index of the first non-repeating character in string s.
    Returns -1 if no unique character exists.
    """
    counts = Counter(s)
    for i, char in enumerate(s):
        if counts[char] == 1:
            return i
    return -1


def is_isomorphic(s: str, t: str) -> bool:
    """
    Checks if characters in s can be replaced to get t, preserving character order.
    No two characters may map to the same character, but a character may map to itself.
    """
    if len(s) != len(t):
        return False
        
    s2t = {}
    t2s = {}
    
    for char_s, char_t in zip(s, t):
        if char_s in s2t and s2t[char_s] != char_t:
            return False
        if char_t in t2s and t2s[char_t] != char_s:
            return False
            
        s2t[char_s] = char_t
        t2s[char_t] = char_s
        
    return True


if __name__ == "__main__":
    # Test Two Sum
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    
    # Test First Unique Character
    assert first_uniq_char("leetcode") == 0
    assert first_uniq_char("loveleetcode") == 2
    assert first_uniq_char("aabb") == -1
    
    # Test Isomorphic Strings
    assert is_isomorphic("egg", "add") is True
    assert is_isomorphic("foo", "bar") is False
    assert is_isomorphic("paper", "title") is True
    
    print("[SUCCESS] All Level 1 Hash Map Basics tests passed!")
