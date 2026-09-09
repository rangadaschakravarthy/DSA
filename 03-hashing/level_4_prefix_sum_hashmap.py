"""
Level 4: Prefix Sum & Hash Map Synthesis

Topics Covered:
1. Subarray Sum Equals K O(N)
2. Subarray Product Less Than K (Sliding Window + Frequency O(N))

Complexity:
- Time Complexity: O(N) single pass.
- Space Complexity: O(N) auxiliary space.
"""

def subarray_sum(nums: list[int], k: int) -> int:
    """Finds total number of continuous subarrays whose sum equals k."""
    prefix_counts = {0: 1}
    current_sum = 0
    count = 0
    
    for num in nums:
        current_sum += num
        if current_sum - k in prefix_counts:
            count += prefix_counts[current_sum - k]
        prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1
        
    return count


def num_subarray_product_less_than_k(nums: list[int], k: int) -> int:
    """
    Finds number of contiguous subarrays where product of all elements is strictly less than k.
    """
    if k <= 1:
        return 0
        
    prod = 1
    left = 0
    count = 0
    
    for right in range(len(nums)):
        prod *= nums[right]
        while prod >= k:
            prod //= nums[left]
            left += 1
        count += (right - left + 1)
        
    return count


if __name__ == "__main__":
    # Test Subarray Sum Equals K
    assert subarray_sum([1, 1, 1], 2) == 2
    assert subarray_sum([1, 2, 3], 3) == 2
    
    # Test Subarray Product Less Than K
    assert num_subarray_product_less_than_k([10, 5, 2, 6], 100) == 8
    
    print("[SUCCESS] All Level 4 Prefix-Sum Hash Map tests passed!")
