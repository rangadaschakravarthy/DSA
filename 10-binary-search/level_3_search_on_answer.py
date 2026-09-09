"""
Level 3: Binary Search on Answer Space

Topics Covered:
1. Koko Eating Bananas O(N log(max_pile))

Pattern Insight:
When searching for an optimal minimum or maximum parameter K:
1. Identify valid search bounds for K: [low, high].
2. Define a monotonic feasibility predicate function `can_finish(k)`.
3. If `can_finish(mid)` is True, try smaller K (high = mid). Else low = mid + 1.
"""

import math

def min_eating_speed(piles: list[int], h: int) -> int:
    """
    Finds minimum integer eating speed k (bananas per hour) such that Koko can eat all bananas within h hours.
    """
    def can_finish(k: int) -> bool:
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / k)
        return hours <= h
        
    low, high = 1, max(piles)
    ans = high
    
    while low <= high:
        mid = low + (high - low) // 2
        if can_finish(mid):
            ans = mid
            high = mid - 1  # Try to find a smaller valid speed
        else:
            low = mid + 1   # Speed too slow, increase speed
            
    return ans


if __name__ == "__main__":
    # Test Koko Eating Bananas
    assert min_eating_speed([3, 6, 7, 11], 8) == 4
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30
    assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23
    
    print("[SUCCESS] All Level 3 Binary Search on Answer tests passed!")
