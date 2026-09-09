"""
Level 2: Jump Game I & II

Problem:
1. Jump Game I: You are initially positioned at index 0. Check if you can reach the last index.
2. Jump Game II: Return the minimum number of jumps to reach the last index.

Time Complexity: O(N)
Space Complexity: O(1)
"""

def can_jump(nums: list[int]) -> bool:
    max_reach = 0
    for i, num in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + num)
    return True


def min_jumps(nums: list[int]) -> int:
    if len(nums) <= 1:
        return 0
    
    jumps = 0
    curr_end = 0
    max_reach = 0
    
    for i in range(len(nums) - 1):
        max_reach = max(max_reach, i + nums[i])
        if i == curr_end:
            jumps += 1
            curr_end = max_reach
            
    return jumps


if __name__ == "__main__":
    assert can_jump([2, 3, 1, 1, 4]) == True
    assert can_jump([3, 2, 1, 0, 4]) == False
    assert min_jumps([2, 3, 1, 1, 4]) == 2
    print("[PASS] Level 2 Jump Game I & II tests passed!")
