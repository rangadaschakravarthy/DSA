"""
Level 8: Greedy Two Pointers & Capacity Limits

Topics Covered:
1. Boats to Save People O(N log N)

Greedy Strategy:
Sort weights. Pair the heaviest person (right) with the lightest person (left) if their combined weight <= limit!
Otherwise, the heaviest person must travel alone in a boat.
"""

def num_rescue_boats(people: list[int], limit: int) -> int:
    """
    Finds minimum number of boats to carry all people given max weight capacity limit per boat (max 2 people per boat).
    """
    people.sort()
    left, right = 0, len(people) - 1
    boats = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1  # Lightest person paired with heaviest
        right -= 1     # Heaviest person allocated to boat
        boats += 1
        
    return boats


if __name__ == "__main__":
    assert num_rescue_boats([1, 2], 3) == 1
    assert num_rescue_boats([3, 2, 2, 1], 3) == 3
    assert num_rescue_boats([3, 5, 3, 4], 5) == 4
    
    print("[SUCCESS] All Level 8 Boats to Save People tests passed!")
