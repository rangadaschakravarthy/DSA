"""
Level 6: Subarray Range Two-Pointer Bounds

Topics Covered:
1. Shortest Unsorted Continuous Subarray O(N) time, O(1) space

Algorithm:
Scan left-to-right maintaining max_seen: find rightmost element smaller than max_seen.
Scan right-to-left maintaining min_seen: find leftmost element larger than min_seen.
"""

def find_unsorted_subarray(nums: list[int]) -> int:
    """
    Finds length of the shortest continuous subarray that, if sorted, sorts the entire array.
    """
    n = len(nums)
    if n <= 1:
        return 0
        
    left_boundary = -1
    right_boundary = -2
    
    max_seen = nums[0]
    for i in range(1, n):
        max_seen = max(max_seen, nums[i])
        if nums[i] < max_seen:
            right_boundary = i
            
    min_seen = nums[-1]
    for i in range(n - 2, -1, -1):
        min_seen = min(min_seen, nums[i])
        if nums[i] > min_seen:
            left_boundary = i
            
    return right_boundary - left_boundary + 1


if __name__ == "__main__":
    assert find_unsorted_subarray([2, 6, 4, 8, 10, 9, 15]) == 5  # Subarray [6, 4, 8, 10, 9]
    assert find_unsorted_subarray([1, 2, 3, 4]) == 0
    assert find_unsorted_subarray([1]) == 0
    
    print("[SUCCESS] All Level 6 Shortest Unsorted Subarray tests passed!")
