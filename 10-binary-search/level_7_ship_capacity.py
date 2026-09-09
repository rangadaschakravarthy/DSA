"""
Level 7: Capacity To Ship Packages Within D Days

Problem:
A conveyor belt has packages that must be shipped within days days.
The ith package on the conveyor belt has a weight of weights[i]. 
Return the least weight capacity of the ship that will result in all the packages being shipped within days days.

Time Complexity: O(N * log(sum(weights)))
Space Complexity: O(1)
"""

def ship_within_days(weights: list[int], days: int) -> int:
    def can_ship(capacity):
        d = 1
        curr_weight = 0
        for w in weights:
            if curr_weight + w > capacity:
                d += 1
                curr_weight = w
            else:
                curr_weight += w
        return d <= days

    left, right = max(weights), sum(weights)
    ans = right
    while left <= right:
        mid = (left + right) // 2
        if can_ship(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans


if __name__ == "__main__":
    assert ship_within_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15
    assert ship_within_days([3, 2, 2, 4, 1, 4], 3) == 6
    print("[PASS] Level 7 Ship Capacity tests passed!")
