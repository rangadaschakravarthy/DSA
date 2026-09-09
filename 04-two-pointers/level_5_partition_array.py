"""
Level 5: In-Place Partitioning & Read/Write Pointers

Topics Covered:
1. Move Zeroes to End In-Place O(N) time, O(1) space
2. Sort Array by Parity (Evens before Odds) O(N) time, O(1) space

Complexity:
- Time Complexity: O(N) single pass.
- Space Complexity: O(1) auxiliary space.
"""

def move_zeroes(nums: list[int]) -> None:
    """
    Moves all 0's to the end of the array while maintaining the relative order of non-zero elements.
    """
    write_idx = 0
    for read_idx in range(len(nums)):
        if nums[read_idx] != 0:
            nums[write_idx], nums[read_idx] = nums[read_idx], nums[write_idx]
            write_idx += 1


def sort_array_by_parity(nums: list[int]) -> list[int]:
    """
    Partitions array so that all even integers come before all odd integers.
    """
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] % 2 > nums[right] % 2:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left] % 2 == 0:
            left += 1
        if nums[right] % 2 == 1:
            right -= 1
    return nums


if __name__ == "__main__":
    arr1 = [0, 1, 0, 3, 12]
    move_zeroes(arr1)
    assert arr1 == [1, 3, 12, 0, 0]
    
    arr2 = [3, 1, 2, 4]
    sorted_parity = sort_array_by_parity(arr2)
    assert sorted_parity[0] % 2 == 0 and sorted_parity[1] % 2 == 0
    
    print("[SUCCESS] All Level 5 Partition Array tests passed!")
