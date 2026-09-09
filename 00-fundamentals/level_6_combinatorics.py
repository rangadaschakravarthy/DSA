"""
Level 6: Advanced Combinatorics & Modular Inverses

Topics Covered:
1. Combinations nCr % MOD using Modular Inverse O(N) prep, O(1) query
2. Pascal's Triangle K-th Row Generation O(K) space

Complexity:
- nCr % MOD: O(N) precomputation, O(1) per query.
- Pascal Row: O(K) space, O(K^2) or O(K) time.
"""

def power_mod(base: int, exp: int, mod: int) -> int:
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result


def mod_inverse(n: int, mod: int) -> int:
    """Computes Fermat's Little Theorem modular inverse: n^(mod - 2) % mod."""
    return power_mod(n, mod - 2, mod)


def nCr_mod(n: int, r: int, mod: int = 10**9 + 7) -> int:
    """Calculates nCr % mod in O(r) time."""
    if r < 0 or r > n:
        return 0
    if r == 0 or r == n:
        return 1
    if r > n // 2:
        r = n - r
        
    num = 1
    den = 1
    for i in range(1, r + 1):
        num = (num * (n - i + 1)) % mod
        den = (den * i) % mod
        
    return (num * mod_inverse(den, mod)) % mod


def pascal_triangle_row(row_index: int) -> list[int]:
    """Generates row_index-th row of Pascal's Triangle using O(K) space."""
    row = [1]
    for i in range(1, row_index + 1):
        # Calculate next element using relationship: C(n, k) = C(n, k-1) * (n - k + 1) // k
        next_val = row[-1] * (row_index - i + 1) // i
        row.append(next_val)
    return row


if __name__ == "__main__":
    # Test nCr % MOD
    MOD = 10**9 + 7
    assert nCr_mod(5, 2, MOD) == 10
    assert nCr_mod(10, 3, MOD) == 120
    
    # Test Pascal Triangle Row
    assert pascal_triangle_row(3) == [1, 3, 3, 1]
    assert pascal_triangle_row(0) == [1]
    
    print("[SUCCESS] All Level 6 Combinatorics tests passed!")
