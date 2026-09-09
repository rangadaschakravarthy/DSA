"""
Level 3: Palindromic Substring Algorithms

Topics Covered:
1. Longest Palindromic Substring (Expand Around Center O(N^2))
2. Count Palindromic Substrings (Odd & Even centers)

Complexity:
- Time Complexity: O(N^2) time.
- Space Complexity: O(1) auxiliary space (no DP table overhead).
"""

def expand_around_center(s: str, left: int, right: int) -> tuple[int, int]:
    """
    Expands outward from center (left, right) as long as characters match.
    Returns (start_index, length) of the palindrome found.
    """
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    # After loop, valid palindrome bounds are (left + 1) to (right - 1)
    return left + 1, right - left - 1


def longest_palindromic_substring(s: str) -> str:
    """
    Finds the longest palindromic substring in s using Expand Around Center.
    Tests 2N - 1 possible centers (N odd centers + N - 1 even centers).
    """
    if not s:
        return ""
        
    start = 0
    max_len = 0
    
    for i in range(len(s)):
        # Odd length palindromes (center at i)
        s1, l1 = expand_around_center(s, i, i)
        # Even length palindromes (center between i and i+1)
        s2, l2 = expand_around_center(s, i, i + 1)
        
        if l1 > max_len:
            start, max_len = s1, l1
        if l2 > max_len:
            start, max_len = s2, l2
            
    return s[start : start + max_len]


def count_palindromic_substrings(s: str) -> int:
    """
    Counts total number of palindromic substrings in s.
    """
    count = 0
    
    def count_from_center(left: int, right: int) -> int:
        c = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            c += 1
            left -= 1
            right += 1
        return c
        
    for i in range(len(s)):
        count += count_from_center(i, i)      # Odd length
        count += count_from_center(i, i + 1)  # Even length
        
    return count


if __name__ == "__main__":
    # Test Longest Palindromic Substring
    assert longest_palindromic_substring("babad") in ["bab", "aba"]
    assert longest_palindromic_substring("cbbd") == "bb"
    
    # Test Count Palindromic Substrings
    assert count_palindromic_substrings("abc") == 3   # "a", "b", "c"
    assert count_palindromic_substrings("aaa") == 6   # "a", "a", "a", "aa", "aa", "aaa"
    
    print("[SUCCESS] All Level 3 Palindrome tests passed!")
