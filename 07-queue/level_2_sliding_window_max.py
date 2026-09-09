"""
Level 2: Monotonic Deque & Sliding Window Maximum

Topics Covered:
1. Sliding Window Maximum O(N) using collections.deque

Monotonic Deque Invariants:
1. Deque stores indices of elements in strictly DECREASING order of their values.
2. The front of the deque (deque[0]) ALWAYS contains the maximum element index for current window.
3. Remove indices out of current window bounds (index <= i - k).
"""

from collections import deque

def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """
    Finds the maximum element in each sliding window of size k moving from left to right.
    """
    if not nums or k == 0:
        return []
        
    q = deque()  # Stores indices
    result = []
    
    for i in range(len(nums)):
        # 1. Remove indices outside current window range [i - k + 1, i]
        if q and q[0] <= i - k:
            q.popleft()
            
        # 2. Maintain Monotonic Decreasing property: pop smaller elements from right
        while q and nums[q[-1]] < nums[i]:
            q.pop()
            
        q.append(i)
        
        # 3. Add max of current window (q[0]) to result once window reaches size k
        if i >= k - 1:
            result.append(nums[q[0]])
            
    return result


if __name__ == "__main__":
    # Test Sliding Window Maximum
    assert max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert max_sliding_window([1], 1) == [1]
    
    print("[SUCCESS] All Level 2 Sliding Window Maximum tests passed!")
