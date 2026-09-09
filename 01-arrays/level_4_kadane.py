"""
Level 4: Kadane's Algorithm & Subarray Optimization

Topics Covered:
1. Maximum Subarray Sum (Kadane's Algorithm)
2. Subarray Index Recovery (Finding exact start & end indices)
3. Maximum Circular Subarray Sum

Complexity:
- Time Complexity: O(N) single pass.
- Space Complexity: O(1) auxiliary space.
"""

def max_subarray_sum(nums: list[int]) -> int:
    """
    Finds the maximum sum of a contiguous subarray using Kadane's Algorithm.
    """
    max_so_far = nums[0]
    current_max = nums[0]
    
    for i in range(1, len(nums)):
        current_max = max(nums[i], current_max + nums[i])
        max_so_far = max(max_so_far, current_max)
        
    return max_so_far


def max_subarray_with_indices(nums: list[int]) -> tuple[int, int, int]:
    """
    Returns (max_sum, start_index, end_index) of the maximum contiguous subarray.
    """
    max_so_far = nums[0]
    current_max = nums[0]
    
    best_start = best_end = temp_start = 0
    
    for i in range(1, len(nums)):
        if nums[i] > current_max + nums[i]:
            current_max = nums[i]
            temp_start = i
        else:
            current_max += nums[i]
            
        if current_max > max_so_far:
            max_so_far = current_max
            best_start = temp_start
            best_end = i
            
    return (max_so_far, best_start, best_end)


def max_circular_subarray_sum(nums: list[int]) -> int:
    """
    Finds maximum subarray sum in a circular array.
    Cases:
    1. Maximum subarray does not wrap -> Standard Kadane's Max
    2. Maximum subarray wraps -> Total Sum - Standard Kadane's Min
    """
    max_sum = min_sum = current_max = current_min = nums[0]
    total_sum = nums[0]
    
    for i in range(1, len(nums)):
        val = nums[i]
        total_sum += val
        
        current_max = max(val, current_max + val)
        max_sum = max(max_sum, current_max)
        
        current_min = min(val, current_min + val)
        min_sum = min(min_sum, current_min)
        
    # If all numbers are negative, max_sum will be negative and total_sum == min_sum
    if max_sum < 0:
        return max_sum
        
    return max(max_sum, total_sum - min_sum)


if __name__ == "__main__":
    # Test Kadane's Algorithm
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6  # Subarray [4, -1, 2, 1]
    
    # Test Kadane's with Indices
    max_sum, start, end = max_subarray_with_indices([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    assert (max_sum, start, end) == (6, 3, 6)
    
    # Test Circular Kadane's
    assert max_circular_subarray_sum([5, -3, 5]) == 10  # Circular [5, 5]
    assert max_circular_subarray_sum([-3, -2, -3]) == -2
    
    print("[SUCCESS] All Level 4 Kadane's Algorithm tests passed!")
