"""
Level 7: Two Pointers Branching & Character Deletion

Topics Covered:
1. Valid Palindrome II (Delete at most 1 character O(N) time, O(1) space)

Logic:
When s[left] != s[right], check if s[left+1..right] OR s[left..right-1] is a palindrome!
"""

def is_palindrome_range(s: str, left: int, right: int) -> bool:
    """Helper to check if substring s[left..right] is a palindrome."""
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def valid_palindrome_ii(s: str) -> bool:
    """
    Checks if string s can become a palindrome after deleting at most one character.
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            # Delete character at left OR delete character at right
            return is_palindrome_range(s, left + 1, right) or is_palindrome_range(s, left, right - 1)
        left += 1
        right -= 1
        
    return True


if __name__ == "__main__":
    assert valid_palindrome_ii("aba") is True
    assert valid_palindrome_ii("abca") is True  # Delete 'c'
    assert valid_palindrome_ii("abc") is False
    
    print("[SUCCESS] All Level 7 Valid Palindrome II tests passed!")
