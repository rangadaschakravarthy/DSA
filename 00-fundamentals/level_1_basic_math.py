"""
Level 1: Basic Math Operations & Number Analysis

Topics Covered:
1. Count Digits & Reverse an Integer
2. Check Palindrome Number
3. Greatest Common Divisor (GCD) / Euclidean Algorithm
4. Least Common Multiple (LCM)

Complexity:
- Time Complexity: O(log10(N)) for digit extraction, O(log(min(a, b))) for GCD.
- Space Complexity: O(1) auxiliary space.
"""

def count_digits(n: int) -> int:
    """Returns number of digits in positive integer n."""
    if n == 0:
        return 1
    n = abs(n)
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count


def reverse_integer(n: int) -> int:
    """Reverses digits of a 32-bit signed integer. Returns 0 on overflow."""
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = 0
    
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
        
    reversed_num *= sign
    # 32-bit integer bounds check
    if reversed_num < -2**31 or reversed_num > 2**31 - 1:
        return 0
    return reversed_num


def is_palindrome_number(n: int) -> bool:
    """Checks if integer n is a palindrome without string conversion."""
    if n < 0 or (n % 10 == 0 and n != 0):
        return False
    return n == reverse_integer(n)


def gcd_euclidean(a: int, b: int) -> int:
    """Computes Greatest Common Divisor using Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Computes Least Common Multiple using relationship: LCM(a, b) = (a * b) // GCD(a, b)."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd_euclidean(a, b)


if __name__ == "__main__":
    # Test Count Digits
    assert count_digits(12345) == 5
    assert count_digits(0) == 1
    
    # Test Reverse Integer
    assert reverse_integer(123) == 321
    assert reverse_integer(-123) == -321
    
    # Test Palindrome Number
    assert is_palindrome_number(121) is True
    assert is_palindrome_number(-121) is False
    
    # Test GCD & LCM
    assert gcd_euclidean(48, 18) == 6
    assert lcm(4, 6) == 12
    
    print("[SUCCESS] All Level 1 Basic Math tests passed!")
