"""
Level 8: Linear-Time Z-Algorithm

Topics Covered:
1. Z-Array Construction O(N)
2. Exact String Matching using Z-Algorithm O(N + M)

Definition:
Z[i] is the length of the longest substring starting from s[i] that is also a prefix of s.
"""

def build_z_array(s: str) -> list[int]:
    """Computes Z-array for string s in O(N) time."""
    n = len(s)
    z = [0] * n
    l, r, k = 0, 0, 0
    
    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and s[r - l] == s[r]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < n and s[r - l] == s[r]:
                    r += 1
                z[i] = r - l
                r -= 1
                
    return z


def z_algorithm_search(text: str, pattern: str) -> list[int]:
    """Finds all occurrences of pattern in text using Z-algorithm."""
    concat = pattern + "$" + text
    z = build_z_array(concat)
    pattern_len = len(pattern)
    matches = []
    
    for i in range(len(concat)):
        if z[i] == pattern_len:
            matches.append(i - pattern_len - 1)
            
    return matches


if __name__ == "__main__":
    # Test Z-Algorithm
    assert z_algorithm_search("baabaa", "aab") == [1]
    assert z_algorithm_search("abcababc", "abc") == [0, 5]
    
    print("[SUCCESS] All Level 8 Z-Algorithm tests passed!")
