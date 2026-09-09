"""
Level 1: Fixed & Semi-Fixed Sliding Window Algorithms

Topics Covered:
1. Maximum Sum Subarray of Size K O(N)
2. Max Consecutive Ones III (Flip at most K zeros) O(N)

Complexity:
- Time Complexity: O(N) single pass.
- Space Complexity: O(1) auxiliary space.
"""

def max_sub_array_of_size_k(arr: list[int], k: int) -> int:
    """
    Finds maximum sum of any contiguous subarray of fixed size k.
    """
    if len(arr) < k:
        return 0
        
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
        
    return max_sum


def longest_ones_flip_k(nums: list[int], k: int) -> int:
    """
    Finds maximum number of consecutive 1s in array if you can flip at most k 0s to 1s.
    Uses variable sliding window maintaining zero_count <= k.
    """
    left = 0
    zero_count = 0
    max_len = 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
            
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
            
        max_len = max(max_len, right - left + 1)
        
    return max_len


if __name__ == "__main__":
    # Test Max Subarray of Size K
    assert max_sub_array_of_size_k([2, 1, 5, 1, 3, 2], 3) == 9  # Subarray [5, 1, 3]
    
    # Test Max Consecutive Ones III
    assert longest_ones_flip_k([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6
    assert longest_ones_flip_k([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3) == 10
    
    print("[SUCCESS] All Level 1 Fixed Window tests passed!")
