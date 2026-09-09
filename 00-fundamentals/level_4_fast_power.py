"""
Level 4: Fast Exponentiation & Modular Arithmetic

Topics Covered:
1. Binary Exponentiation (Fast Power) O(log N)
2. Modular Exponentiation (pow(base, exp, mod))
3. Modular Inverse & Division under modulo

Complexity:
- Time Complexity: O(log N)
- Space Complexity: O(1) iterative space.
"""

def fast_power(base: float, exp: int) -> float:
    """Computes base^exp in O(log N) time using binary exponentiation."""
    if exp < 0:
        base = 1 / base
        exp = -exp
        
    result = 1.0
    current_product = base
    
    while exp > 0:
        if exp % 2 == 1:
            result *= current_product
        current_product *= current_product
        exp //= 2
        
    return result


def power_mod(base: int, exp: int, mod: int) -> int:
    """Computes (base^exp) % mod safely without integer overflow."""
    if mod == 1:
        return 0
        
    result = 1
    base = base % mod
    
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
        
    return result


if __name__ == "__main__":
    # Test Fast Power
    assert abs(fast_power(2.0, 10) - 1024.0) < 1e-6
    assert abs(fast_power(2.0, -2) - 0.25) < 1e-6
    
    # Test Modular Exponentiation
    assert power_mod(2, 10, 1000) == 24
    assert power_mod(3, 45, 7) == power_mod(3, 45 % 6, 7)  # Fermat's Little Theorem property
    
    print("[SUCCESS] All Level 4 Fast Power tests passed!")
