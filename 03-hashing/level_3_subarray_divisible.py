"""
Level 3: Advanced Prefix Sum & Modular Hash Map Patterns

Topics Covered:
1. Subarray Sums Divisible by K O(N)
2. Contiguous Array with Equal Number of 0s and 1s O(N)

Complexity:
- Subarrays Divisible by K: O(N) time, O(K) space for remainder map.
- Equal 0s and 1s: O(N) time, O(N) space.
"""

def subarrays_div_by_k(nums: list[int], k: int) -> int:
    """
    Finds total number of non-empty continuous subarrays whose sum is divisible by k.
    
    Key Math Property:
    If prefix_sum[j] % k == prefix_sum[i] % k, then sum(nums[i+1...j]) is divisible by k.
    """
    remainder_counts = {0: 1}  # Base case: empty prefix has sum 0 (remainder 0)
    current_sum = 0
    total_subarrays = 0
    
    for num in nums:
        current_sum += num
        remainder = current_sum % k
        # Normalize negative remainder in Python (Python's % operator naturally handles negatives)
        
        if remainder in remainder_counts:
            total_subarrays += remainder_counts[remainder]
            
        remainder_counts[remainder] = remainder_counts.get(remainder, 0) + 1
        
    return total_subarrays


def find_max_length_equal_zeros_ones(nums: list[int]) -> int:
    """
    Finds maximum length of a contiguous subarray with an equal number of 0s and 1s.
    
    Transformation:
    Replace 0 with -1. Problem reduces to finding longest subarray with sum 0!
    """
    first_seen = {0: -1}  # prefix_sum -> first index seen
    current_sum = 0
    max_len = 0
    
    for i, num in enumerate(nums):
        current_sum += 1 if num == 1 else -1
        
        if current_sum in first_seen:
            max_len = max(max_len, i - first_seen[current_sum])
        else:
            first_seen[current_sum] = i
            
    return max_len


if __name__ == "__main__":
    # Test Subarray Sums Divisible by K
    assert subarrays_div_by_k([4, 5, 0, -2, -3, 1], 5) == 7
    assert subarrays_div_by_k([5], 9) == 0
    
    # Test Equal 0s and 1s
    assert find_max_length_equal_zeros_ones([0, 1]) == 2
    assert find_max_length_equal_zeros_ones([0, 1, 0]) == 2
    assert find_max_length_equal_zeros_ones([0, 0, 1, 0, 0, 0, 1, 1]) == 6
    
    print("[SUCCESS] All Level 3 Subarray Divisible tests passed!")
