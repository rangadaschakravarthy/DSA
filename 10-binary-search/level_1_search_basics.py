"""
Level 1: Binary Search Foundations & Boundary Bounds

Topics Covered:
1. Standard Binary Search O(log N)
2. First and Last Position of Element in Sorted Array (Lower & Upper Bound O(log N))

Complexity:
- Time Complexity: O(log N)
- Space Complexity: O(1) iterative space.
"""

def binary_search(nums: list[int], target: int) -> int:
    """
    Standard binary search in a sorted array. Returns index if found, else -1.
    """
    low, high = 0, len(nums) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1


def find_lower_bound(nums: list[int], target: int) -> int:
    """Finds first index where nums[index] >= target."""
    low, high = 0, len(nums) - 1
    ans = -1
    
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] >= target:
            if nums[mid] == target:
                ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans


def find_upper_bound(nums: list[int], target: int) -> int:
    """Finds last index where nums[index] <= target."""
    low, high = 0, len(nums) - 1
    ans = -1
    
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] <= target:
            if nums[mid] == target:
                ans = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return ans


def search_range(nums: list[int], target: int) -> list[int]:
    """
    Finds starting and ending position of a given target value in a sorted array.
    """
    first = find_lower_bound(nums, target)
    last = find_upper_bound(nums, target)
    return [first, last]


if __name__ == "__main__":
    # Test Standard Binary Search
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1
    
    # Test First and Last Position
    assert search_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert search_range([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert search_range([], 0) == [-1, -1]
    
    print("[SUCCESS] All Level 1 Binary Search tests passed!")
