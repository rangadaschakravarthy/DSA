"""
Level 4: Advanced String Sliding Window Algorithms

Topics Covered:
1. Longest Substring Without Repeating Characters O(N)
2. Minimum Window Substring O(N)

Complexity:
- Time Complexity: O(N) single pass.
- Space Complexity: O(min(N, Alphabet_Size)) space.
"""

from collections import Counter

def length_of_longest_substring(s: str) -> int:
    """
    Finds length of longest substring without repeating characters using variable sliding window.
    Stores last seen index of each character for jump-optimization.
    """
    char_index_map = {}
    max_len = 0
    left = 0
    
    for right, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= left:
            left = char_index_map[char] + 1
            
        char_index_map[char] = right
        max_len = max(max_len, right - left + 1)
        
    return max_len


def min_window_substring(s: str, t: str) -> str:
    """
    Finds the minimum window substring of s such that every character in t (including duplicates) is included.
    Returns empty string if no such window exists.
    """
    if not s or not t:
        return ""
        
    target_counts = Counter(t)
    required_unique = len(target_counts)
    
    window_counts = {}
    formed_unique = 0
    
    # (window_len, left_idx, right_idx)
    ans = (float('inf'), None, None)
    left = 0
    
    for right, char in enumerate(s):
        window_counts[char] = window_counts.get(char, 0) + 1
        
        if char in target_counts and window_counts[char] == target_counts[char]:
            formed_unique += 1
            
        # Try shrinking window from left once all characters are matched
        while left <= right and formed_unique == required_unique:
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
                
            left_char = s[left]
            window_counts[left_char] -= 1
            
            if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                formed_unique -= 1
                
            left += 1
            
    return "" if ans[0] == float('inf') else s[ans[1] : ans[2] + 1]


if __name__ == "__main__":
    # Test Longest Substring Without Repeating Characters
    assert length_of_longest_substring("abcabcbb") == 3   # "abc"
    assert length_of_longest_substring("bbbbb") == 1      # "b"
    assert length_of_longest_substring("pwwkew") == 3     # "wke"
    
    # Test Minimum Window Substring
    assert min_window_substring("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window_substring("a", "a") == "a"
    assert min_window_substring("a", "aa") == ""
    
    print("[SUCCESS] All Level 4 Window Substring tests passed!")
