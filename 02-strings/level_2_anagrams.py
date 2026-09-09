"""
Level 2: Anagram Patterns & Frequency Mapping

Topics Covered:
1. Valid Anagram Check O(N)
2. Group Anagrams using Frequency Tuple Hashing O(N * K)
3. Find All Anagrams in a String (Fixed Sliding Window + Frequency Array)

Complexity:
- Valid Anagram: O(N) time, O(1) space (alphabet size 26).
- Group Anagrams: O(N * K) time where K is max string length.
- Find All Anagrams: O(N) time, O(1) space.
"""

from collections import defaultdict

def is_anagram(s: str, t: str) -> bool:
    """
    Checks if string t is an anagram of s.
    """
    if len(s) != len(t):
        return False
        
    counts = [0] * 26
    for char_s, char_t in zip(s, t):
        counts[ord(char_s) - ord('a')] += 1
        counts[ord(char_t) - ord('a')] -= 1
        
    return all(c == 0 for c in counts)


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Groups anagrams together using character count tuple (26 elements) as dictionary key.
    Avoids string sorting O(K log K) per word!
    """
    groups = defaultdict(list)
    
    for s in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        # Use tuple of 26 integers as hashable map key
        groups[tuple(count)].append(s)
        
    return list(groups.values())


def find_anagrams_in_string(s: str, p: str) -> list[int]:
    """
    Finds all start indices of p's anagrams in s.
    Uses fixed sliding window of size len(p).
    """
    if len(p) > len(s):
        return []
        
    p_count = [0] * 26
    s_count = [0] * 26
    
    for i in range(len(p)):
        p_count[ord(p[i]) - ord('a')] += 1
        s_count[ord(s[i]) - ord('a')] += 1
        
    result = []
    if s_count == p_count:
        result.append(0)
        
    window_size = len(p)
    for i in range(window_size, len(s)):
        # Add new character entering window
        s_count[ord(s[i]) - ord('a')] += 1
        # Remove old character leaving window
        s_count[ord(s[i - window_size]) - ord('a')] -= 1
        
        if s_count == p_count:
            result.append(i - window_size + 1)
            
    return result


if __name__ == "__main__":
    # Test Valid Anagram
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    
    # Test Group Anagrams
    grouped = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # Sort groups for deterministic assertion
    sorted_groups = sorted([sorted(g) for g in grouped])
    assert sorted_groups == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    
    # Test Find All Anagrams
    assert find_anagrams_in_string("cbaebabacd", "abc") == [0, 6]
    
    print("[SUCCESS] All Level 2 Anagram tests passed!")
