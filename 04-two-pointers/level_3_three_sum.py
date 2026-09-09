"""
Level 3: Two Pointers - 3Sum Triplet Search

Topics Covered:
1. 3Sum (Unique triplets adding up to 0 O(N^2) time, O(1) extra space)

Complexity:
- Time Complexity: O(N^2)
- Space Complexity: O(1) auxiliary space (excluding output).
"""

def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Finds all unique triplets [nums[i], nums[j], nums[k]] such that nums[i] + nums[j] + nums[k] == 0.
    """
    nums.sort()
    triplets = []
    n = len(nums)
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        target = -nums[i]
        left, right = i + 1, n - 1
        
        while left < right:
            two_sum = nums[left] + nums[right]
            if two_sum == target:
                triplets.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif two_sum < target:
                left += 1
            else:
                right -= 1
                
    return triplets


if __name__ == "__main__":
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    print("[SUCCESS] All Level 3 3Sum tests passed!")
