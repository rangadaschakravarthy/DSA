"""
Level 9: Count of Smaller Numbers After Self (BST / MergeSort Approach)

Problem:
Given an integer array nums, return an integer array counts where counts[i] 
is the number of smaller elements to the right of nums[i].

Time Complexity: O(N log N)
Space Complexity: O(N)
"""

def count_smaller(nums: list[int]) -> list[int]:
    n = len(nums)
    counts = [0] * n
    indices = list(range(n))

    def merge_sort(enum_indices):
        half = len(enum_indices) // 2
        if half:
            left, right = merge_sort(enum_indices[:half]), merge_sort(enum_indices[half:])
            for i in range(len(enum_indices) - 1, -1, -1):
                if not right or (left and nums[left[-1]] > nums[right[-1]]):
                    counts[left[-1]] += len(right)
                    enum_indices[i] = left.pop()
                else:
                    enum_indices[i] = right.pop()
        return enum_indices

    merge_sort(indices)
    return counts


if __name__ == "__main__":
    assert count_smaller([5, 2, 6, 1]) == [2, 1, 1, 0]
    assert count_smaller([-1]) == [0]
    assert count_smaller([-1, -1]) == [0, 0]
    print("[PASS] Level 9 Count of Smaller Numbers After Self tests passed!")
