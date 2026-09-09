"""
Level 6: Variable Window with Flip/Replace Constraints

Topics Covered:
1. Max Consecutive Ones III (Flip at most K zeros O(N) time, O(1) space)

Complexity:
- Time Complexity: O(N) single pass.
- Space Complexity: O(1) auxiliary space.
"""

def longest_ones(nums: list[int], k: int) -> int:
    """
    Finds the maximum number of consecutive 1s if you can flip at most k 0s.
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
    assert longest_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6
    assert longest_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3) == 10
    
    print("[SUCCESS] All Level 6 Max Consecutive Ones tests passed!")
