"""
Level 2: Prefix Sum Array & Hash Map Combinations

Topics Covered:
1. Prefix Sum Array Construction & Range Sum Query O(1)
2. Pivot Index (Equilibrium Point where Left Sum == Right Sum)
3. Subarray Sum Equals K (Prefix Sum + Hash Map)

Complexity:
- Range Sum Query: O(N) preprocessing, O(1) per query.
- Subarray Sum Equals K: O(N) time, O(N) space.
"""

class PrefixSum1D:
    """Class for performing fast O(1) range sum queries on an array."""
    
    def __init__(self, nums: list[int]):
        # prefix[i] stores sum of nums[0...i-1]
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def query_range(self, left: int, right: int) -> int:
        """Returns sum of elements from index left to right (inclusive)."""
        return self.prefix[right + 1] - self.prefix[left]


def find_pivot_index(nums: list[int]) -> int:
    """
    Finds the leftmost pivot index where sum of left elements equals sum of right elements.
    Returns -1 if no such index exists.
    """
    total_sum = sum(nums)
    left_sum = 0
    
    for i, num in enumerate(nums):
        if left_sum == total_sum - left_sum - num:
            return i
        left_sum += num
        
    return -1


def subarray_sum_equals_k(nums: list[int], k: int) -> int:
    """
    Finds total number of continuous subarrays whose sum equals k.
    Uses Prefix Sum + Hash Map pattern.
    """
    prefix_counts = {0: 1}  # Base case: empty prefix has sum 0
    current_sum = 0
    count = 0
    
    for num in nums:
        current_sum += num
        # If (current_sum - k) was seen before, those prefix windows sum to k
        if (current_sum - k) in prefix_counts:
            count += prefix_counts[current_sum - k]
            
        prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1
        
    return count


if __name__ == "__main__":
    # Test 1D Prefix Sum Query
    nums1 = [-2, 0, 3, -5, 2, -1]
    ps = PrefixSum1D(nums1)
    assert ps.query_range(0, 2) == 1   # (-2) + 0 + 3 = 1
    assert ps.query_range(2, 5) == -1  # 3 + (-5) + 2 + (-1) = -1
    assert ps.query_range(0, 5) == -3
    
    # Test Pivot Index
    assert find_pivot_index([1, 7, 3, 6, 5, 6]) == 3  # Left: 1+7+3=11, Right: 5+6=11
    assert find_pivot_index([1, 2, 3]) == -1
    
    # Test Subarray Sum Equals K
    assert subarray_sum_equals_k([1, 1, 1], 2) == 2
    assert subarray_sum_equals_k([1, -1, 0], 0) == 3
    
    print("[SUCCESS] All Level 2 Prefix Sum tests passed!")
