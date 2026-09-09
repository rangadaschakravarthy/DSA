"""
Level 2: Sequence Problems & Set Lookups

Topics Covered:
1. Longest Consecutive Sequence O(N) using Hash Set
2. Contains Nearby Duplicate II O(N) using Sliding Hash Set

Complexity:
- Longest Consecutive: O(N) time (each number visited at most twice), O(N) space.
- Nearby Duplicate: O(N) time, O(min(N, K)) space.
"""

def longest_consecutive(nums: list[int]) -> int:
    """
    Finds the length of the longest consecutive elements sequence in an unsorted array.
    Must run in O(N) time.
    
    Key Insight:
    Only start building a sequence if `num - 1` is NOT in the set!
    This guarantees each element is processed at most twice.
    """
    num_set = set(nums)
    longest_streak = 0
    
    for num in num_set:
        # Check if num is the START of a consecutive sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
                
            longest_streak = max(longest_streak, current_streak)
            
    return longest_streak


def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    """
    Checks if there exist two distinct indices i and j such that nums[i] == nums[j] and abs(i - j) <= k.
    Uses sliding hash set of size k.
    """
    window = set()
    
    for i, num in enumerate(nums):
        if num in window:
            return True
        window.add(num)
        if len(window) > k:
            window.remove(nums[i - k])
            
    return False


if __name__ == "__main__":
    # Test Longest Consecutive Sequence
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4     # Sequence [1, 2, 3, 4]
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    
    # Test Contains Nearby Duplicate
    assert contains_nearby_duplicate([1, 2, 3, 1], 3) is True
    assert contains_nearby_duplicate([1, 0, 1, 1], 1) is True
    assert contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2) is False
    
    print("[SUCCESS] All Level 2 Consecutive Sequence tests passed!")
