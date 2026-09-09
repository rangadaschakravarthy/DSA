"""
Level 1: String Basics & Two-Pointer Verification

Topics Covered:
1. Valid Palindrome (Ignoring non-alphanumeric characters and case)
2. Longest Common Prefix (Vertical Scan)
3. Reverse Words in a String

Complexity:
- Valid Palindrome: O(N) time, O(1) space.
- Longest Common Prefix: O(S) time (S = total chars in all strings), O(1) space.
- Reverse Words: O(N) time, O(N) space.
"""

def is_valid_palindrome(s: str) -> bool:
    """
    Checks if string is a palindrome considering only alphanumeric characters and ignoring case.
    Uses Two Pointers.
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
            
        if s[left].lower() != s[right].lower():
            return False
            
        left += 1
        right -= 1
        
    return True


def longest_common_prefix(strs: list[str]) -> str:
    """
    Finds the longest common prefix string among an array of strings.
    """
    if not strs:
        return ""
        
    # Vertical scanning
    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != char:
                return strs[0][:i]
                
    return strs[0]


def reverse_words(s: str) -> str:
    """
    Reverses the order of words in a string, stripping leading/trailing and excess internal spaces.
    """
    words = s.strip().split()
    return " ".join(reversed(words))


if __name__ == "__main__":
    # Test Valid Palindrome
    assert is_valid_palindrome("A man, a plan, a canal: Panama") is True
    assert is_valid_palindrome("race a car") is False
    
    # Test Longest Common Prefix
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""
    
    # Test Reverse Words
    assert reverse_words("  the sky  is blue  ") == "blue is sky the"
    
    print("[SUCCESS] All Level 1 String Basics tests passed!")
