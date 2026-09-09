"""
Level 6: 2D Matrix Maximal Rectangle via Histogram Stack

Topics Covered:
1. Maximal Rectangle in 2D Binary Matrix O(M * N)

Algorithm:
1. Convert each row of 2D binary matrix into a 1D Histogram of heights.
2. Run Largest Rectangle in Histogram (Monotonic Stack) for each row!
"""

def largest_rectangle_area(heights: list[int]) -> int:
    """Helper: Largest Rectangle in Histogram."""
    stack = []
    max_area = 0
    padded = heights + [0]
    
    for i, h in enumerate(padded):
        while stack and padded[stack[-1]] > h:
            height = padded[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
        
    return max_area


def maximal_rectangle(matrix: list[list[str]]) -> int:
    """
    Finds area of largest rectangle containing only '1's in a 2D binary matrix.
    """
    if not matrix or not matrix[0]:
        return 0
        
    cols = len(matrix[0])
    heights = [0] * cols
    max_area = 0
    
    for row in matrix:
        for c in range(cols):
            heights[c] = heights[c] + 1 if row[c] == '1' else 0
        max_area = max(max_area, largest_rectangle_area(heights))
        
    return max_area


if __name__ == "__main__":
    matrix = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
    assert maximal_rectangle(matrix) == 6
    assert maximal_rectangle([["0"]]) == 0
    assert maximal_rectangle([["1"]]) == 1
    
    print("[SUCCESS] All Level 6 Maximal Rectangle tests passed!")
