"""
Level 1: Fast & Slow Pointers (Floyd's Cycle Detection)

Topics Covered:
1. Find the Duplicate Number in array of N+1 integers (Floyd's Cycle Finding O(N) time, O(1) space)
2. Happy Number Verification O(log N) time, O(1) space

Complexity:
- Find Duplicate: O(N) time, O(1) space without modifying array.
- Happy Number: O(log N) time, O(1) space.
"""

def find_duplicate(nums: list[int]) -> int:
    """
    Finds duplicate number in nums containing N + 1 integers where each integer is in range [1, N].
    Uses Floyd's Cycle Detection Algorithm (Tortoise and Hare).
    
    Phase 1: Find intersection point of slow and fast pointers.
    Phase 2: Find entrance to cycle (duplicate number).
    """
    slow = nums[0]
    fast = nums[0]
    
    # Phase 1: Detect cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
            
    # Phase 2: Find cycle entry point
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
        
    return slow


def get_sum_of_squares(n: int) -> int:
    """Helper function to return sum of squares of digits of n."""
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10
    return total


def is_happy_number(n: int) -> bool:
    """
    Determines if n is a Happy Number.
    Uses Fast & Slow pointers to detect loops without extra set memory.
    """
    slow = n
    fast = get_sum_of_squares(n)
    
    while fast != 1 and slow != fast:
        slow = get_sum_of_squares(slow)
        fast = get_sum_of_squares(get_sum_of_squares(fast))
        
    return fast == 1


if __name__ == "__main__":
    # Test Find Duplicate Number
    assert find_duplicate([1, 3, 4, 2, 2]) == 2
    assert find_duplicate([3, 1, 3, 4, 2]) == 3
    
    # Test Happy Number
    assert is_happy_number(19) is True   # 19 -> 82 -> 68 -> 100 -> 1
    assert is_happy_number(2) is False   # Cycles endlessly
    
    print("[SUCCESS] All Level 1 Fast & Slow Pointers tests passed!")
