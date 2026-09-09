"""
Level 9: Extended Euclidean Algorithm & Chinese Remainder Theorem (CRT)

Problem:
1. Extended Euclidean Algorithm: Find integers x, y such that a*x + b*y = gcd(a, b).
2. Chinese Remainder Theorem (CRT): Solve system of simultaneous congruences:
   x ≡ r1 (mod m1)
   x ≡ r2 (mod m2)
   ...
   where moduli m1, m2 are pairwise coprime.

Time Complexity: O(N log(max(M)))
Space Complexity: O(1)
"""

def ext_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Returns (g, x, y) such that a*x + b*y = g = gcd(a, b).
    """
    if b == 0:
        return a, 1, 0
    g, x1, y1 = ext_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


def mod_inverse(a: int, m: int) -> int:
    """
    Returns modular multiplicative inverse of a modulo m using Extended GCD.
    """
    g, x, _ = ext_gcd(a, m)
    if g != 1:
        raise ValueError("Modular inverse does not exist")
    return (x % m + m) % m


def chinese_remainder_theorem(num: list[int], rem: list[int]) -> int:
    """
    Solves x ≡ rem[i] (mod num[i]) for pairwise coprime num[i].
    Returns smallest non-negative integer x.
    """
    prod = 1
    for n in num:
        prod *= n

    result = 0
    for i in range(len(num)):
        pp = prod // num[i]
        inv = mod_inverse(pp, num[i])
        result += rem[i] * inv * pp

    return result % prod


if __name__ == "__main__":
    # Test Extended GCD: 35*x + 15*y = 5 -> 35*(1) + 15*(-2) = 5
    g, x, y = ext_gcd(35, 15)
    assert g == 5
    assert 35 * x + 15 * y == 5

    # Test Modular Inverse: (3 * x) % 11 == 1 -> x = 4
    assert mod_inverse(3, 11) == 4

    # Test Chinese Remainder Theorem:
    # x ≡ 2 (mod 3)
    # x ≡ 3 (mod 5)
    # x ≡ 2 (mod 7)
    # Solution x = 23
    num = [3, 5, 7]
    rem = [2, 3, 2]
    assert chinese_remainder_theorem(num, rem) == 23

    print("[PASS] Level 9 Extended GCD & Chinese Remainder Theorem tests passed!")
