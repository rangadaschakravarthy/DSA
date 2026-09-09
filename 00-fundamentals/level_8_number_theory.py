"""
Level 8: Advanced Number Theory & Euler's Totient

Topics Covered:
1. Euler's Totient Function phi(N) O(sqrt(N))
2. Segmented Sieve for Range Primes [L, R]

Mathematics:
phi(N) counts integers k in 1 <= k <= N such that gcd(k, N) = 1.
Formula: phi(N) = N * product(1 - 1/p) for distinct prime factors p of N.
"""

import math

def euler_totient(n: int) -> int:
    """Calculates Euler's Totient Function phi(n) in O(sqrt(N)) time."""
    result = n
    p = 2
    temp = n
    
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
        
    if temp > 1:
        result -= result // temp
        
    return result


def simple_sieve(limit: int) -> list[int]:
    """Helper to generate primes up to limit."""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.isqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(2, limit + 1) if is_prime[i]]


def segmented_sieve(low: int, high: int) -> list[int]:
    """Finds all prime numbers in range [low, high] using Segmented Sieve."""
    if low < 2:
        low = 2
        
    limit = int(math.isqrt(high)) + 1
    primes = simple_sieve(limit)
    
    is_prime = [True] * (high - low + 1)
    
    for p in primes:
        # Find minimum multiple of p >= low
        start = max(p * p, ((low + p - 1) // p) * p)
        for j in range(start, high + 1, p):
            is_prime[j - low] = False
            
    return [low + i for i in range(len(is_prime)) if is_prime[i]]


if __name__ == "__main__":
    # Test Euler's Totient
    assert euler_totient(10) == 4   # 1, 3, 7, 9 are coprime to 10
    assert euler_totient(12) == 4   # 1, 5, 7, 11 are coprime to 12
    assert euler_totient(13) == 12  # Prime n: phi(n) = n - 1
    
    # Test Segmented Sieve
    assert segmented_sieve(10, 30) == [11, 13, 17, 19, 23, 29]
    
    print("[SUCCESS] All Level 8 Number Theory tests passed!")
