"""
Level 9: Create Maximum Number

Problem:
You are given two integer arrays nums1 and nums2 of lengths m and n respectively. 
Create the maximum number of length k <= m + n from digits of the two numbers 
while preserving the relative order of digits in each array.

Time Complexity: O(K * (M + N)^2)
Space Complexity: O(K)
"""

def max_number(nums1: list[int], nums2: list[int], k: int) -> list[int]:
    def max_single_array(nums, k_len):
        drop = len(nums) - k_len
        stack = []
        for num in nums:
            while drop and stack and stack[-1] < num:
                stack.pop()
                drop -= 1
            stack.append(num)
        return stack[:k_len]

    def merge(seq1, seq2):
        return [max(seq1, seq2).pop(0) for _ in range(len(seq1) + len(seq2))]

    res = []
    m, n = len(nums1), len(nums2)
    for i in range(max(0, k - n), min(k, m) + 1):
        s1 = max_single_array(nums1, i)
        s2 = max_single_array(nums2, k - i)
        merged = merge(s1, s2)
        res = max(res, merged)
        
    return res


if __name__ == "__main__":
    nums1 = [3, 4, 6, 5]
    nums2 = [9, 1, 2, 5, 8, 3]
    assert max_number(nums1, nums2, 5) == [9, 8, 6, 5, 3]
    print("[PASS] Level 9 Create Maximum Number tests passed!")
