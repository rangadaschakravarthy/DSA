"""
Level 4: Multi-Pointer Quadruplets (4Sum)

Topics Covered:
1. 4Sum (Unique quadruplets adding up to target O(N^3) time, O(1) space)

Complexity:
- Time Complexity: O(N^3)
- Space Complexity: O(1) auxiliary space (excluding output).
"""

def four_sum(nums: list[int], target: int) -> list[list[int]]:
    """
    Finds all unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that sum equals target.
    """
    nums.sort()
    quadruplets = []
    n = len(nums)
    
    for a in range(n - 3):
        if a > 0 and nums[a] == nums[a - 1]:
            continue
            
        for b in range(a + 1, n - 2):
            if b > a + 1 and nums[b] == nums[b - 1]:
                continue
                
            left, right = b + 1, n - 1
            curr_target = target - nums[a] - nums[b]
            
            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum == curr_target:
                    quadruplets.append([nums[a], nums[b], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif two_sum < curr_target:
                    left += 1
                else:
                    right -= 1
                    
    return quadruplets


if __name__ == "__main__":
    assert four_sum([1, 0, -1, 0, -2, 2], 0) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    print("[SUCCESS] All Level 4 4Sum tests passed!")
