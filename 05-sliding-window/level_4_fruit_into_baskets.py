"""
Level 4: Fruit Into Baskets (At Most 2 Types Window)

Topics Covered:
1. Fruit Into Baskets O(N) time, O(1) space

Complexity:
- Time Complexity: O(N) single pass.
- Space Complexity: O(1) (at most 2 entries in frequency map).
"""

def total_fruit(fruits: list[int]) -> int:
    """
    Finds maximum number of fruits you can pick into 2 baskets (at most 2 fruit types).
    """
    basket = {}
    left = 0
    max_fruits = 0
    
    for right, fruit in enumerate(fruits):
        basket[fruit] = basket.get(fruit, 0) + 1
        
        while len(basket) > 2:
            left_fruit = fruits[left]
            basket[left_fruit] -= 1
            if basket[left_fruit] == 0:
                del basket[left_fruit]
            left += 1
            
        max_fruits = max(max_fruits, right - left + 1)
        
    return max_fruits


if __name__ == "__main__":
    assert total_fruit([1, 2, 1]) == 3
    assert total_fruit([0, 1, 2, 2]) == 3  # Subarray [1, 2, 2]
    assert total_fruit([1, 2, 3, 2, 2]) == 4  # Subarray [2, 3, 2, 2]
    
    print("[SUCCESS] All Level 4 Fruit Into Baskets tests passed!")
