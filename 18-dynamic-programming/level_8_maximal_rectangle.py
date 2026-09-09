"""
Level 8: Maximal Rectangle in Binary Matrix

Problem:
Given a rows x cols binary matrix filled with 0's and 1's, 
find the largest rectangle containing only 1's and return its area.

Time Complexity: O(R * C)
Space Complexity: O(C) histogram array
"""

def maximal_rectangle(matrix: list[list[str]]) -> int:
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * (cols + 1)
    max_area = 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == '1':
                heights[c] += 1
            else:
                heights[c] = 0

        # Largest Rectangle in Histogram using monotonic stack
        stack = [-1]
        for c in range(cols + 1):
            while stack and heights[c] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = c - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(c)

    return max_area


if __name__ == "__main__":
    mat = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
    assert maximal_rectangle(mat) == 6
    assert maximal_rectangle([["0"]]) == 0
    assert maximal_rectangle([["1"]]) == 1
    print("[PASS] Level 8 Maximal Rectangle tests passed!")
