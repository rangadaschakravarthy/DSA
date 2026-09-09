"""
Level 3: Advanced Monotonic Stack & Histogram Problems

Topics Covered:
1. Largest Rectangle in Histogram O(N)

Algorithm:
Maintain a stack of indices with strictly increasing heights.
When a smaller height is encountered, pop from stack and calculate area with the popped height as the shortest bar!
Width = current_index - stack[-1] - 1 (or current_index if stack is empty).
"""

def largest_rectangle_area(heights: list[int]) -> int:
    """
    Finds the area of the largest rectangle in a histogram.
    """
    stack = []  # Stores indices of histogram bars
    max_area = 0
    heights_padded = heights + [0]  # Append 0 to flush remaining bars at the end
    
    for i, h in enumerate(heights_padded):
        while stack and heights_padded[stack[-1]] > h:
            height = heights_padded[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
        
    return max_area


if __name__ == "__main__":
    # Test Largest Rectangle in Histogram
    assert largest_rectangle_area([2, 1, 5, 6, 2, 3]) == 10  # Bars 5 and 6 form area 5 * 2 = 10
    assert largest_rectangle_area([2, 4]) == 4
    
    print("[SUCCESS] All Level 3 Histogram tests passed!")
