"""
Level 9: DP + Monotonic Deque Optimization (Mastery Level)

Topics Covered:
1. Constrained Subsequence Sum O(N) time, O(N) space

DP State:
dp[i] = max subsequence sum ending at index i such that dist(i, j) <= k.
dp[i] = nums[i] + max(0, max_{i-k <= j < i} dp[j]).
Monotonic Deque tracks max dp[j] in sliding window of size k!
"""

from collections import deque

def constrained_subset_sum(nums: list[int], k: int) -> int:
    """
    Finds maximum sum of a non-empty subsequence of nums such that for every two consecutive
    elements in the subsequence, nums[i] and nums[j], the distance |i - j| <= k.
    """
    dp = [0] * len(nums)
    q = deque()  # Monotonic decreasing deque storing indices of max dp values
    max_sum = float('-inf')
    
    for i, num in enumerate(nums):
        # 1. Remove indices out of range [i - k, i - 1]
        if q and q[0] < i - k:
            q.popleft()
            
        # 2. Compute dp[i]
        max_prev_dp = dp[q[0]] if q else 0
        dp[i] = num + max(0, max_prev_dp)
        max_sum = max(max_sum, dp[i])
        
        # 3. Maintain Monotonic Decreasing property in deque
        while q and dp[q[-1]] <= dp[i]:
            q.pop()
            
        q.append(i)
        
    return max_sum


if __name__ == "__main__":
    assert constrained_subset_sum([10, 2, -10, 5, 20], 2) == 37  # [10, 2, 5, 20]
    assert constrained_subset_sum([-1, -2, -3], 1) == -1
    assert constrained_subset_sum([10, -2, -10, -5, 20], 2) == 23  # [10, -2, 20] or [10, 20] if distance allows
    
    print("[SUCCESS] All Level 9 Constrained Subsequence Sum Mastery tests passed!")
