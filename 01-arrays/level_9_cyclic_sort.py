"""
Level 9: Mastery Level Cyclic Sort & In-Place Array Indexing

Topics Covered:
1. First Missing Positive O(N) time, O(1) space
2. Find All Duplicates in an Array O(N) time, O(1) space

Cyclic Sort Pattern:
When array numbers are in range [1, N], each element belongs at index (val - 1).
Swap elements to their correct positions in O(N) total swaps!
"""

def first_missing_positive(nums: list[int]) -> int:
    """
    Finds the smallest missing positive integer in an unsorted array.
    Must run in O(N) time and O(1) auxiliary space.
    """
    n = len(nums)
    i = 0
    
    while i < n:
        correct_idx = nums[i] - 1
        # Place nums[i] at correct index if in range [1, n] and not duplicate
        if 1 <= nums[i] <= n and nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1
            
    for idx in range(n):
        if nums[idx] != idx + 1:
            return idx + 1
            
    return n + 1


def find_all_duplicates(nums: list[int]) -> list[list[int]]:
    """
    Finds all elements appearing twice in an array where 1 <= nums[i] <= n.
    Uses sign-flipping index marking.
    """
    result = []
    for num in nums:
        idx = abs(num) - 1
        if nums[idx] < 0:
            result.append(abs(num))
        else:
            nums[idx] = -nums[idx]
    return sorted(result)


if __name__ == "__main__":
    # Test First Missing Positive
    assert first_missing_positive([1, 2, 0]) == 3
    assert first_missing_positive([3, 4, -1, 1]) == 2
    assert first_missing_positive([7, 8, 9, 11, 12]) == 1
    
    # Test Find All Duplicates
    assert find_all_duplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]
    
    print("[SUCCESS] All Level 9 Cyclic Sort Mastery tests passed!")
