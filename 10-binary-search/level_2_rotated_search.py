"""
Level 2: Search in Rotated Sorted Arrays

Topics Covered:
1. Search in Rotated Sorted Array O(log N)
2. Find Minimum in Rotated Sorted Array O(log N)

Key Insight:
At least one half of a rotated sorted array (low...mid or mid...high) is ALWAYS strictly sorted!
Determine which half is sorted, then check if target falls within that sorted range.
"""

def search_rotated(nums: list[int], target: int) -> int:
    """
    Searches for target in a rotated sorted array of unique values.
    Returns index if found, else -1.
    """
    low, high = 0, len(nums) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
            
        # Check if left half is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Otherwise, right half must be sorted
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
                
    return -1


def find_min_rotated(nums: list[int]) -> int:
    """
    Finds the minimum element in a rotated sorted array of unique values.
    """
    low, high = 0, len(nums) - 1
    
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] > nums[high]:
            # Minimum must be in right half (excluding mid)
            low = mid + 1
        else:
            # Minimum is at mid or in left half
            high = mid
            
    return nums[low]


if __name__ == "__main__":
    # Test Search in Rotated Array
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search_rotated([1], 0) == -1
    
    # Test Find Minimum in Rotated Array
    assert find_min_rotated([3, 4, 5, 1, 2]) == 1
    assert find_min_rotated([4, 5, 6, 7, 0, 1, 2]) == 0
    assert find_min_rotated([11, 13, 15, 17]) == 11
    
    print("[SUCCESS] All Level 2 Rotated Search tests passed!")
