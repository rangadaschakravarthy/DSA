"""
Level 1: Greedy Reachability & Jump Games

Topics Covered:
1. Jump Game I (Check if last index is reachable O(N) time, O(1) space)
2. Jump Game II (Find minimum jumps to reach last index O(N) time, O(1) space)

Greedy Choice:
At each index, greedily update the furthest index that can be reached from current range!
"""

def can_jump(nums: list[int]) -> bool:
    """
    Returns True if you can reach the last index starting from index 0.
    """
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False  # Cannot reach index i
        max_reach = max(max_reach, i + jump)
        if max_reach >= len(nums) - 1:
            return True
    return True


def min_jumps(nums: list[int]) -> int:
    """
    Finds the minimum number of jumps to reach the last index.
    Uses Greedy BFS-level boundary expansion.
    """
    if len(nums) <= 1:
        return 0
        
    jumps = 0
    current_end = 0
    furthest = 0
    
    for i in range(len(nums) - 1):
        furthest = max(furthest, i + nums[i])
        
        # When we reach the end of the current jump level, increment jump count
        if i == current_end:
            jumps += 1
            current_end = furthest
            if current_end >= len(nums) - 1:
                break
                
    return jumps


if __name__ == "__main__":
    # Test Jump Game I
    assert can_jump([2, 3, 1, 1, 4]) is True
    assert can_jump([3, 2, 1, 0, 4]) is False
    
    # Test Jump Game II
    assert min_jumps([2, 3, 1, 1, 4]) == 2
    assert min_jumps([2, 3, 0, 1, 4]) == 2
    
    print("[SUCCESS] All Level 1 Jump Game tests passed!")
