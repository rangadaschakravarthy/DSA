"""
Level 5: Dutch National Flag Algorithm & 3-Way Partitioning

Topics Covered:
1. Sort Colors (Sort array of 0s, 1s, and 2s in one pass)
2. 3-Way Array Partitioning around an arbitrary Pivot

Complexity:
- Time Complexity: O(N) single pass with 3 pointers (low, mid, high).
- Space Complexity: O(1) in-place auxiliary space.
"""

def sort_colors(nums: list[int]) -> None:
    """
    Sorts an array containing only 0s, 1s, and 2s in-place in a single pass.
    
    Pointers Invariant:
    - Everything before low is 0.
    - Everything between low and mid - 1 is 1.
    - Everything after high is 2.
    """
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


def three_way_partition(nums: list[int], low_val: int, high_val: int) -> None:
    """
    Partitions nums in-place into three ranges:
    1. Elements < low_val come first.
    2. Elements between low_val and high_val come next.
    3. Elements > high_val come last.
    """
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] < low_val:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] > high_val:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
        else:
            mid += 1


if __name__ == "__main__":
    # Test Sort Colors
    arr1 = [2, 0, 2, 1, 1, 0]
    sort_colors(arr1)
    assert arr1 == [0, 0, 1, 1, 2, 2]
    
    # Test 3-Way Partitioning around Range [10, 20]
    arr2 = [1, 14, 5, 20, 4, 11, 30, 50, 100]
    three_way_partition(arr2, 10, 20)
    # Check elements < 10 come first, then 10-20, then > 20
    idx = 0
    while idx < len(arr2) and arr2[idx] < 10:
        idx += 1
    while idx < len(arr2) and 10 <= arr2[idx] <= 20:
        idx += 1
    while idx < len(arr2) and arr2[idx] > 20:
        idx += 1
    assert idx == len(arr2)
    
    print("[SUCCESS] All Level 5 Dutch National Flag tests passed!")
