"""
Level 6: Koko Eating Bananas

Problem:
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.
Return the minimum integer speed k (bananas-per-hour) such that Koko can eat all bananas within h hours.

Time Complexity: O(N * log(max(piles)))
Space Complexity: O(1)
"""
import math

def min_eating_speed(piles: list[int], h: int) -> int:
    def can_eat_all(speed):
        hours = 0
        for p in piles:
            hours += math.ceil(p / speed)
        return hours <= h

    left, right = 1, max(piles)
    ans = right
    while left <= right:
        mid = (left + right) // 2
        if can_eat_all(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans


if __name__ == "__main__":
    assert min_eating_speed([3, 6, 7, 11], 8) == 4
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30
    assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23
    print("[PASS] Level 6 Koko Eating Bananas tests passed!")
