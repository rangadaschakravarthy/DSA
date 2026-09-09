"""
Level 9: Sliding Window Median (Mastery Level)

Topics Covered:
1. Sliding Window Median O(N log K) using Bisect Sorted Window

Complexity:
- Time Complexity: O(N log K) maintaining sorted window of size K.
- Space Complexity: O(K) for window storage.
"""

import bisect

def median_sliding_window(nums: list[int], k: int) -> list[float]:
    """
    Finds median of each sliding window of size k moving left to right.
    """
    window = sorted(nums[:k])
    medians = []
    
    def get_median():
        if k % 2 == 1:
            return float(window[k // 2])
        else:
            return (window[k // 2 - 1] + window[k // 2]) / 2.0
            
    medians.append(get_median())
    
    for i in range(k, len(nums)):
        # Remove exiting element nums[i - k]
        window.remove(nums[i - k])
        # Insert entering element nums[i] in sorted order
        bisect.insort(window, nums[i])
        medians.append(get_median())
        
    return medians


if __name__ == "__main__":
    assert median_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
    
    print("[SUCCESS] All Level 9 Sliding Window Median tests passed!")
