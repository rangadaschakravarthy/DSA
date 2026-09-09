"""
Level 3: Find First and Last Position of Element in Sorted Array

Problem:
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found, return [-1, -1].

Time Complexity: O(log N)
Space Complexity: O(1)
"""

def search_range(nums: list[int], target: int) -> list[int]:
    def find_bound(is_first):
        left, right = 0, len(nums) - 1
        bound = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                bound = mid
                if is_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return bound

    return [find_bound(True), find_bound(False)]


if __name__ == "__main__":
    assert search_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert search_range([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    print("[PASS] Level 3 Find First and Last Position tests passed!")
