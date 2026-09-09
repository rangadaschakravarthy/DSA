"""
Level 2: Bitwise Manipulation Fundamentals

Topics Covered:
1. Bitwise Operators: AND (&), OR (|), XOR (^), NOT (~), Left Shift (<<), Right Shift (>>)
2. Single Number (Find element appearing once when others appear twice)
3. Count Set Bits (Hamming Weight)
4. Check if Number is Power of Two

Complexity:
- Time Complexity: O(1) or O(log2(N)) bit operations.
- Space Complexity: O(1) auxiliary space.
"""

def is_power_of_two(n: int) -> bool:
    """Checks if n is a power of two using n & (n - 1) property."""
    return n > 0 and (n & (n - 1)) == 0


def count_set_bits(n: int) -> int:
    """Counts number of 1-bits (Hamming Weight) using Brian Kernighan's Algorithm."""
    n = abs(n)
    count = 0
    while n > 0:
        n &= (n - 1)  # Clears the lowest set bit
        count += 1
    return count


def single_number(nums: list[int]) -> int:
    """
    Finds element appearing once in array where every other element appears twice.
    Uses XOR property: x ^ x = 0 and x ^ 0 = x.
    """
    result = 0
    for num in nums:
        result ^= num
    return result


def get_bit(n: int, i: int) -> int:
    """Returns the i-th bit of n (0-indexed from right)."""
    return (n >> i) & 1


def set_bit(n: int, i: int) -> int:
    """Sets the i-th bit of n to 1."""
    return n | (1 << i)


def clear_bit(n: int, i: int) -> int:
    """Clears the i-th bit of n (sets to 0)."""
    return n & ~(1 << i)


if __name__ == "__main__":
    # Test Power of Two
    assert is_power_of_two(16) is True
    assert is_power_of_two(18) is False
    assert is_power_of_two(1) is True
    
    # Test Count Set Bits
    assert count_set_bits(7) == 3   # 7 = 0b111
    assert count_set_bits(16) == 1  # 16 = 0b10000
    
    # Test Single Number
    assert single_number([4, 1, 2, 1, 2]) == 4
    
    # Test Bit Operations
    assert get_bit(5, 0) == 1  # 5 = 0b101
    assert set_bit(5, 1) == 7  # 5 | 0b010 = 0b111 (7)
    assert clear_bit(7, 1) == 5 # 7 & ~0b010 = 0b101 (5)
    
    print("[SUCCESS] All Level 2 Bit Manipulation tests passed!")
