"""
Level 9: Suffix Array Mastery & Longest Common Substring

Topics Covered:
1. Suffix Array Construction O(N log N)
2. Longest Common Substring using Suffix Array Concept O(N log N)

Mastery String Data Structures:
A suffix array contains sorted starting indices of all suffixes of string s.
"""

def build_suffix_array(s: str) -> list[int]:
    """Generates suffix array (sorted indices of suffixes) for string s."""
    suffixes = [(s[i:], i) for i in range(len(s))]
    suffixes.sort(key=lambda x: x[0])
    return [suffix[1] for suffix in suffixes]


def longest_common_substring(s1: str, s2: str) -> str:
    """
    Finds the longest common substring between s1 and s2 using Suffix Array concept.
    Concat: s1 + '#' + s2 + '$'
    """
    concat = s1 + "#" + s2 + "$"
    n1 = len(s1)
    sa = build_suffix_array(concat)
    
    max_len = 0
    lcs = ""
    
    def lcp_length(i, j):
        length = 0
        while i < len(concat) and j < len(concat) and concat[i] == concat[j]:
            length += 1
            i += 1
            j += 1
        return length
        
    for i in range(len(sa) - 1):
        idx1, idx2 = sa[i], sa[i + 1]
        # Check if one suffix belongs to s1 and the other to s2
        if (idx1 < n1 and idx2 > n1) or (idx1 > n1 and idx2 < n1):
            l = lcp_length(idx1, idx2)
            if l > max_len:
                max_len = l
                lcs = concat[idx1 : idx1 + l]
                
    return lcs


if __name__ == "__main__":
    # Test Suffix Array
    assert build_suffix_array("banana") == [5, 3, 1, 0, 4, 2]  # "a", "ana", "anana", "banana", "na", "nana"
    
    # Test Longest Common Substring
    assert longest_common_substring("ABABC", "BABCA") == "BABC"
    
    print("[SUCCESS] All Level 9 Suffix Array Mastery tests passed!")
