"""
Level 8: Median of Two Sorted Arrays

Problem:
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Time Complexity: O(log(min(M, N)))
Space Complexity: O(1)
"""

def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
        
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    half_len = (m + n + 1) // 2
    
    while left <= right:
        i = (left + right) // 2
        j = half_len - i
        
        nums1_left = nums1[i - 1] if i > 0 else float('-inf')
        nums1_right = nums1[i] if i < m else float('inf')
        nums2_left = nums2[j - 1] if j > 0 else float('-inf')
        nums2_right = nums2[j] if j < n else float('inf')
        
        if nums1_left <= nums2_right and nums2_left <= nums1_right:
            if (m + n) % 2 == 1:
                return float(max(nums1_left, nums2_left))
            else:
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2.0
        elif nums1_left > nums2_right:
            right = i - 1
        else:
            left = i + 1
            
    return 0.0


if __name__ == "__main__":
    assert find_median_sorted_arrays([1, 3], [2]) == 2.0
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5
    print("[PASS] Level 8 Median of Two Sorted Arrays tests passed!")
