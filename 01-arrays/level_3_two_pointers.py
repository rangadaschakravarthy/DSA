"""
Level 3: Two Pointers Pattern in Arrays

Topics Covered:
1. Two Sum II - Input Array Is Sorted (Opposite Pointers)
2. Container With Most Water (Greedy Two Pointers)
3. 3Sum Problem (Sorting + Two Pointers)

Complexity:
- Two Sum Sorted: O(N) time, O(1) space.
- Container Water: O(N) time, O(1) space.
- 3Sum: O(N^2) time, O(1) auxiliary space (excluding output).
"""

def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    """
    Finds 1-indexed positions of two numbers in sorted array that add up to target.
    """
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
            
    return []


def max_area_container(height: list[int]) -> int:
    """
    Finds two lines that together with x-axis form a container holding the most water.
    Uses greedy shrinking of the container from both ends.
    """
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, width * h)
        
        # Move the pointer pointing to the shorter vertical line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_water


def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Finds all unique triplets [nums[i], nums[j], nums[k]] such that i != j != k and nums[i] + nums[j] + nums[k] == 0.
    """
    nums.sort()
    triplets = []
    n = len(nums)
    
    for i in range(n - 2):
        # Skip duplicate values for the first element
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
                # Skip duplicates for second and third elements
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
    # Test Two Sum Sorted
    assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2]
    
    # Test Container With Most Water
    assert max_area_container([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    
    # Test 3Sum
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    
    print("[SUCCESS] All Level 3 Two Pointers tests passed!")
