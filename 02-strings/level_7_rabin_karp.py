"""
Level 7: Rabin-Karp Rolling Hash Algorithm

Topics Covered:
1. Rolling Hash Precomputation & Matching O(N + M) average time

Polynomial Rolling Hash:
hash(S) = (S[0]*d^(m-1) + S[1]*d^(m-2) + ... + S[m-1]*d^0) % q
"""

def rabin_karp_search(text: str, pattern: str, d: int = 256, q: int = 101) -> list[int]:
    """
    Finds all 0-indexed starting occurrences of pattern in text using Rabin-Karp algorithm.
    """
    m = len(pattern)
    n = len(text)
    if m == 0 or m > n:
        return []
        
    p_hash = 0  # Hash value for pattern
    t_hash = 0  # Hash value for text window
    h = 1       # Value of d^(m-1) % q
    matches = []
    
    for _ in range(m - 1):
        h = (h * d) % q
        
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q
        
    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i : i + m] == pattern:
                matches.append(i)
                
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if t_hash < 0:
                t_hash += q
                
    return matches


if __name__ == "__main__":
    # Test Rabin-Karp Search
    text = "GEEKS FOR GEEKS"
    pattern = "GEEK"
    assert rabin_karp_search(text, pattern) == [0, 10]
    
    print("[SUCCESS] All Level 7 Rabin-Karp Rolling Hash tests passed!")
