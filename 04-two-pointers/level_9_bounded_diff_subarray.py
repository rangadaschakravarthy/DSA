"""
Level 9: Hybrid Two-Pointer Monotonic Deque (Mastery Level)

Topics Covered:
1. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit O(N)

Complexity:
- Time Complexity: O(N) single pass.
- Space Complexity: O(N) for monotonic min/max deques.
"""

from collections import deque

def longest_subarray_bounded_diff(nums: list[int], limit: int) -> int:
    """
    Finds the length of the longest continuous subarray such that the absolute difference
    between any two elements in this subarray is <= limit.
    """
    max_q = deque()  # Monotonic decreasing deque for maximums
    min_q = deque()  # Monotonic increasing deque for minimums
    
    left = 0
    max_len = 0
    
    for right in range(len(nums)):
        val = nums[right]
        
        while max_q and nums[max_q[-1]] < val:
            max_q.pop()
        while min_q and nums[min_q[-1]] > val:
            min_q.pop()
            
        max_q.append(right)
        min_q.append(right)
        
        # Shrink left pointer if diff limit is violated
        while nums[max_q[0]] - nums[min_q[0]] > limit:
            left += 1
            if max_q[0] < left:
                max_q.popleft()
            if min_q[0] < left:
                min_q.popleft()
                
        max_len = max(max_len, right - left + 1)
        
    return max_len


if __name__ == "__main__":
    assert longest_subarray_bounded_diff([8, 2, 4, 7], 4) == 2  # Subarray [2, 4] or [4, 7]
    assert longest_subarray_bounded_diff([10, 1, 2, 4, 7, 2], 5) == 4  # Subarray [2, 4, 7, 2]
    
    print("[SUCCESS] All Level 9 Bounded Diff Subarray Mastery tests passed!")
