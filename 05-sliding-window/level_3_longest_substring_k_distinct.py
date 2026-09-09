"""
Level 3: Longest Substring with At Most K Distinct Characters

Topics Covered:
1. Longest Substring with At Most K Distinct Characters O(N) time, O(K) space

Complexity:
- Time Complexity: O(N) single pass with sliding window.
- Space Complexity: O(K) for character frequency map.
"""

def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    """
    Finds the length of the longest substring of s that contains at most k distinct characters.
    """
    if k == 0 or not s:
        return 0
        
    counts = {}
    left = 0
    max_len = 0
    
    for right, char in enumerate(s):
        counts[char] = counts.get(char, 0) + 1
        
        while len(counts) > k:
            left_char = s[left]
            counts[left_char] -= 1
            if counts[left_char] == 0:
                del counts[left_char]
            left += 1
            
        max_len = max(max_len, right - left + 1)
        
    return max_len


if __name__ == "__main__":
    assert length_of_longest_substring_k_distinct("eceba", 2) == 3  # Substring "ece"
    assert length_of_longest_substring_k_distinct("aa", 1) == 2
    
    print("[SUCCESS] All Level 3 Sliding Window K-Distinct tests passed!")
