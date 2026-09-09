"""
Level 8: Interview / Competitive Programming Array Logic

Topics Covered:
1. Next Permutation (In-Place Lexicographical Swap O(N) time, O(1) space)

Algorithm Steps:
1. Find largest index i such that nums[i] < nums[i + 1] (pivot point).
2. If no such i exists, array is in descending order -> reverse entire array to get smallest permutation.
3. Find largest index j > i such that nums[j] > nums[i].
4. Swap nums[i] and nums[j].
5. Reverse suffix starting at index i + 1.
"""

def next_permutation(nums: list[int]) -> None:
    """
    Rearranges numbers into the lexicographically next greater permutation of numbers in-place.
    """
    n = len(nums)
    if n <= 1:
        return
        
    # Step 1: Find pivot index i
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
        
    if i >= 0:
        # Step 2: Find index j > i to swap with
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        
    # Step 3: Reverse suffix after pivot i
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


if __name__ == "__main__":
    # Test Next Permutation
    arr1 = [1, 2, 3]
    next_permutation(arr1)
    assert arr1 == [1, 3, 2]
    
    arr2 = [3, 2, 1]
    next_permutation(arr2)
    assert arr2 == [1, 2, 3]
    
    arr3 = [1, 1, 5]
    next_permutation(arr3)
    assert arr3 == [1, 5, 1]
    
    print("[SUCCESS] All Level 8 Next Permutation tests passed!")
