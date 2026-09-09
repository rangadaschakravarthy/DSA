"""
Level 8: Monotonic Stack Boundary Trapping

Topics Covered:
1. Trapping Rain Water using Monotonic Decreasing Stack O(N) time, O(N) space

Logic:
Stack stores indices of decreasing bar heights.
When encountering a taller bar, pop the bottom bar `mid = stack.pop()`.
Bounded Height = min(height[current], height[stack[-1]]) - height[mid].
Bounded Width = current - stack[-1] - 1.
"""

def trap_stack(height: list[int]) -> int:
    """Calculates trapped rainwater using a Monotonic Stack."""
    stack = []
    total_water = 0
    
    for i, h in enumerate(height):
        while stack and h > height[stack[-1]]:
            mid_idx = stack.pop()
            if not stack:
                break  # No left boundary to trap water
            left_idx = stack[-1]
            
            bounded_height = min(h, height[left_idx]) - height[mid_idx]
            bounded_width = i - left_idx - 1
            total_water += bounded_height * bounded_width
            
        stack.append(i)
        
    return total_water


if __name__ == "__main__":
    assert trap_stack([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trap_stack([4, 2, 0, 3, 2, 5]) == 9
    
    print("[SUCCESS] All Level 8 Monotonic Stack Rain Water tests passed!")
