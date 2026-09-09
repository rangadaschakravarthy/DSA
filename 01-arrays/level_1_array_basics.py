"""
Level 1: Array Fundamentals & Basic Manipulation

Topics Covered:
1. Reverse an Array In-Place
2. Rotate Array by K Steps (Right & Left)
3. Remove Duplicates from Sorted Array

Complexity:
- Time Complexity: O(N)
- Space Complexity: O(1) auxiliary space (in-place).
"""

def reverse_array_in_place(nums: list[int], start: int = 0, end: int = None) -> None:
    """Reverses elements in nums between index start and end in-place."""
    if end is None:
        end = len(nums) - 1
        
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


def rotate_array_right(nums: list[int], k: int) -> None:
    """
    Rotates array to the right by k steps in-place.
    Uses 3-step reversal technique:
    1. Reverse entire array.
    2. Reverse first k elements.
    3. Reverse remaining n-k elements.
    """
    n = len(nums)
    if n == 0:
        return
    k %= n
    
    reverse_array_in_place(nums, 0, n - 1)
    reverse_array_in_place(nums, 0, k - 1)
    reverse_array_in_place(nums, k, n - 1)


def remove_duplicates_sorted(nums: list[int]) -> int:
    """
    Removes duplicates in-place from sorted array.
    Returns the number of unique elements (k). The first k elements of nums will contain unique values.
    """
    if not nums:
        return 0
        
    write_idx = 1
    for read_idx in range(1, len(nums)):
        if nums[read_idx] != nums[read_idx - 1]:
            nums[write_idx] = nums[read_idx]
            write_idx += 1
            
    return write_idx


if __name__ == "__main__":
    # Test In-Place Reversal
    arr1 = [1, 2, 3, 4, 5]
    reverse_array_in_place(arr1)
    assert arr1 == [5, 4, 3, 2, 1]
    
    # Test Right Rotation
    arr2 = [1, 2, 3, 4, 5, 6, 7]
    rotate_array_right(arr2, 3)
    assert arr2 == [5, 6, 7, 1, 2, 3, 4]
    
    # Test Remove Duplicates
    arr3 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    new_len = remove_duplicates_sorted(arr3)
    assert new_len == 5
    assert arr3[:5] == [0, 1, 2, 3, 4]
    
    print("[SUCCESS] All Level 1 Array Basics tests passed!")
