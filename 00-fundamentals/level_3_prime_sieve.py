"""
Level 3: Prime Numbers & Sieve of Eratosthenes

Topics Covered:
1. Trial Division Prime Check O(sqrt(N))
2. Sieve of Eratosthenes O(N log log N)
3. Prime Factorization O(sqrt(N))

Complexity:
- Check Prime: O(sqrt(N))
- Sieve: O(N log log N) time, O(N) space
"""

def is_prime(n: int) -> bool:
    """Checks if n is prime using trial division up to sqrt(n)."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def sieve_of_eratosthenes(n: int) -> list[int]:
    """Generates all prime numbers up to n (inclusive)."""
    if n < 2:
        return []
    
    is_prime_arr = [True] * (n + 1)
    is_prime_arr[0] = is_prime_arr[1] = False
    
    p = 2
    while p * p <= n:
        if is_prime_arr[p]:
            for i in range(p * p, n + 1, p):
                is_prime_arr[i] = False
        p += 1
        
    return [i for i in range(2, n + 1) if is_prime_arr[i]]


def prime_factors(n: int) -> list[int]:
    """Finds all prime factors of n."""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


if __name__ == "__main__":
    # Test Prime Check
    assert is_prime(29) is True
    assert is_prime(1) is False
    assert is_prime(4) is False
    
    # Test Sieve
    assert sieve_of_eratosthenes(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    
    # Test Prime Factorization
    assert prime_factors(60) == [2, 2, 3, 5]
    
    print("[SUCCESS] All Level 3 Prime Sieve tests passed!")
