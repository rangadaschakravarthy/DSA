"""
Level 6: KMP (Knuth-Morris-Pratt) Pattern Matching

Topics Covered:
1. LPS (Longest Prefix Suffix) Precomputation O(M)
2. KMP String Search Algorithm O(N + M)

Complexity:
- Time Complexity: O(N + M) where N = len(text), M = len(pattern).
- Space Complexity: O(M) for LPS array.
"""

def build_lps(pattern: str) -> list[int]:
    """Computes Longest Prefix Suffix (LPS) array for pattern."""
    lps = [0] * len(pattern)
    length = 0  # Length of previous longest prefix suffix
    i = 1
    
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
                
    return lps


def kmp_search(text: str, pattern: str) -> list[int]:
    """
    Finds all 0-indexed starting occurrences of pattern in text.
    """
    if not pattern:
        return []
        
    lps = build_lps(pattern)
    matches = []
    i = 0  # Index for text
    j = 0  # Index for pattern
    
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
            
        if j == len(pattern):
            matches.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
                
    return matches


if __name__ == "__main__":
    # Test KMP Search
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    assert kmp_search(text, pattern) == [10]
    
    assert kmp_search("aaaaa", "bba") == []
    assert kmp_search("sadbutsad", "sad") == [0, 6]
    
    print("[SUCCESS] All Level 6 KMP Pattern Matching tests passed!")
