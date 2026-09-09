"""
Level 8: Monotonic Deque & Prefix Sum Optimization

Topics Covered:
1. Shortest Subarray with Sum at Least K O(N) time, O(N) space

Complexity:
- Time Complexity: O(N) single pass.
- Space Complexity: O(N) for prefix sum array and deque.
"""

from collections import deque

def shortest_subarray_sum_at_least_k(nums: list[int], k: int) -> int:
    """
    Finds length of shortest non-empty contiguous subarray with sum at least k.
    Handles negative numbers using Prefix Sum + Monotonic Increasing Deque.
    """
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]
        
    q = deque()  # Stores indices of prefix array
    min_len = float('inf')
    
    for i in range(n + 1):
        # 1. Check if valid subarray found: prefix[i] - prefix[q[0]] >= k
        while q and prefix[i] - prefix[q[0]] >= k:
            min_len = min(min_len, i - q.popleft())
            
        # 2. Maintain Monotonic Increasing property in deque
        while q and prefix[i] <= prefix[q[-1]]:
            q.pop()
            
        q.append(i)
        
    return min_len if min_len != float('inf') else -1


if __name__ == "__main__":
    assert shortest_subarray_sum_at_least_k([1], 1) == 1
    assert shortest_subarray_sum_at_least_k([1, 2], 4) == -1
    assert shortest_subarray_sum_at_least_k([2, -1, 2], 3) == 3
    
    print("[SUCCESS] All Level 8 Shortest Subarray Sum K tests passed!")
