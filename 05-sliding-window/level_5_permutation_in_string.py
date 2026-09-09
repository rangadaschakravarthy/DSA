"""
Level 5: Fixed Frequency Window Matching

Topics Covered:
1. Permutation in String O(N) time, O(1) space

Complexity:
- Time Complexity: O(N) single pass.
- Space Complexity: O(1) frequency count array of size 26.
"""

def check_inclusion(s1: str, s2: str) -> bool:
    """
    Returns True if s2 contains a permutation of s1.
    """
    n1, n2 = len(s1), len(s2)
    if n1 > n2:
        return False
        
    s1_count = [0] * 26
    s2_count = [0] * 26
    
    for i in range(n1):
        s1_count[ord(s1[i]) - ord('a')] += 1
        s2_count[ord(s2[i]) - ord('a')] += 1
        
    if s1_count == s2_count:
        return True
        
    for i in range(n1, n2):
        s2_count[ord(s2[i]) - ord('a')] += 1
        s2_count[ord(s2[i - n1]) - ord('a')] -= 1
        if s1_count == s2_count:
            return True
            
    return False


if __name__ == "__main__":
    assert check_inclusion("ab", "eidbaooo") is True  # Contains "ba"
    assert check_inclusion("ab", "eidboaoo") is False
    
    print("[SUCCESS] All Level 5 Permutation in String tests passed!")
