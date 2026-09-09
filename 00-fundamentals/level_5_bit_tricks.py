"""
Level 5: Advanced Bit Manipulation Tricks & Subsets

Topics Covered:
1. Single Number II (Every element appears 3 times except one) O(N) time, O(1) space
2. Single Number III (Two elements appear once, others twice) O(N) time, O(1) space
3. Generate all bitmasks for subsets of size N

Complexity:
- Time Complexity: O(N) or O(2^N) for subset bitmasking.
- Space Complexity: O(1) auxiliary space.
"""

def single_number_ii(nums: list[int]) -> int:
    """
    Finds element appearing once where every other element appears 3 times.
    Uses bitwise state transitions: ones and twos.
    """
    ones, twos = 0, 0
    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones
    return ones


def single_number_iii(nums: list[int]) -> list[int]:
    """
    Finds two unique elements that appear once, where all other elements appear twice.
    Uses XOR sum and lowest set bit partition.
    """
    xor_sum = 0
    for num in nums:
        xor_sum ^= num
        
    # Get rightmost set bit
    diff_bit = xor_sum & (-xor_sum)
    
    num1, num2 = 0, 0
    for num in nums:
        if num & diff_bit:
            num1 ^= num
        else:
            num2 ^= num
            
    return sorted([num1, num2])


def generate_bitmask_subsets(n: int) -> list[list[int]]:
    """Generates all 2^N bitmask subsets for set of size N."""
    subsets = []
    total = 1 << n
    for mask in range(total):
        subset = [i for i in range(n) if (mask & (1 << i))]
        subsets.append(subset)
    return subsets


if __name__ == "__main__":
    # Test Single Number II
    assert single_number_ii([2, 2, 3, 2]) == 3
    assert single_number_ii([0, 1, 0, 1, 0, 1, 99]) == 99
    
    # Test Single Number III
    assert single_number_iii([1, 2, 1, 3, 2, 5]) == [3, 5]
    
    # Test Bitmask Subsets
    assert len(generate_bitmask_subsets(3)) == 8
    
    print("[SUCCESS] All Level 5 Bit Tricks tests passed!")
