"""
Level 2: Trapping Rain Water & Boundary Two Pointers

Topics Covered:
1. Trapping Rain Water O(N) time, O(1) space with Two Pointers

Complexity:
- Time Complexity: O(N) single pass.
- Space Complexity: O(1) auxiliary space.
"""

def trap_rain_water(height: list[int]) -> int:
    """
    Calculates total units of rainwater trapped between elevation bars.
    
    Two Pointers Invariant:
    Water trapped at index i is determined by min(left_max, right_max) - height[i].
    We can advance the pointer with the smaller boundary max!
    """
    if not height:
        return 0
        
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    total_water = 0
    
    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            total_water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            total_water += right_max - height[right]
            
    return total_water


if __name__ == "__main__":
    # Test Trapping Rain Water
    assert trap_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trap_rain_water([4, 2, 0, 3, 2, 5]) == 9
    
    print("[SUCCESS] All Level 2 Trapping Rain Water tests passed!")
