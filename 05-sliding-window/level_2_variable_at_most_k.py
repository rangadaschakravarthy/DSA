"""
Level 2: Variable Window & At-Most-K Pattern

Topics Covered:
1. Subarrays with K Different Integers (At-Most-K Pattern) O(N)

Pattern Insight:
Exact(K) = AtMost(K) - AtMost(K - 1)
Calculating exact K directly with sliding window is difficult because shrinking left boundary might lose valid subarrays.
AtMost(K) counts total valid subarrays ending at index right with <= K distinct elements.
"""

from collections import defaultdict

def at_most_k_distinct(nums: list[int], k: int) -> int:
    """
    Helper function to count continuous subarrays with AT MOST k distinct integers.
    """
    if k <= 0:
        return 0
        
    counts = defaultdict(int)
    left = 0
    total_subarrays = 0
    
    for right in range(len(nums)):
        if counts[nums[right]] == 0:
            k -= 1
        counts[nums[right]] += 1
        
        while k < 0:
            counts[nums[left]] -= 1
            if counts[nums[left]] == 0:
                k += 1
            left += 1
            
        # Number of valid subarrays ending at index right is (right - left + 1)
        total_subarrays += (right - left + 1)
        
    return total_subarrays


def subarrays_with_k_distinct(nums: list[int], k: int) -> int:
    """
    Finds total number of continuous subarrays with EXACTLY k different integers.
    Uses relationship: Exact(K) = AtMost(K) - AtMost(K - 1).
    """
    return at_most_k_distinct(nums, k) - at_most_k_distinct(nums, k - 1)


if __name__ == "__main__":
    # Test Subarrays with K Different Integers
    assert subarrays_with_k_distinct([1, 2, 1, 2, 3], 2) == 7
    assert subarrays_with_k_distinct([1, 2, 1, 3, 4], 3) == 3
    
    print("[SUCCESS] All Level 2 At-Most-K Sliding Window tests passed!")
