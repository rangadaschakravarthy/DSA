"""
Level 6: 2D Matrix Manipulations & Searching

Topics Covered:
1. Rotate N x N Matrix 90 Degrees Clockwise In-Place (Transpose + Reverse Rows)
2. Spiral Traversal of M x N Matrix
3. Search in 2D Matrix II (Row-wise & Column-wise Sorted Matrix)

Complexity:
- Matrix Rotation: O(N^2) time, O(1) in-place space.
- Spiral Traversal: O(M * N) time, O(1) extra space.
- Search 2D Matrix: O(M + N) time starting from top-right corner.
"""

def rotate_matrix_clockwise(matrix: list[list[int]]) -> None:
    """
    Rotates an N x N matrix 90 degrees clockwise in-place.
    Step 1: Transpose matrix (swap matrix[i][j] and matrix[j][i]).
    Step 2: Reverse each row.
    """
    n = len(matrix)
    
    # Step 1: Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()


def spiral_order(matrix: list[list[int]]) -> list[int]:
    """
    Returns all elements of an M x N matrix in spiral order.
    """
    if not matrix or not matrix[0]:
        return []
        
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Traverse Left to Right along Top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        
        # Traverse Top to Bottom along Right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        
        # Traverse Right to Left along Bottom row (if top <= bottom)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
            
        # Traverse Bottom to Top along Left column (if left <= right)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
            
    return result


def search_matrix_2d(matrix: list[list[int]], target: int) -> bool:
    """
    Searches for target in an M x N matrix where:
    - Integers in each row are sorted from left to right.
    - Integers in each column are sorted from top to bottom.
    
    Starts search from top-right corner (row 0, col N-1).
    """
    if not matrix or not matrix[0]:
        return False
        
    row, col = 0, len(matrix[0]) - 1
    
    while row < len(matrix) and col >= 0:
        val = matrix[row][col]
        if val == target:
            return True
        elif val > target:
            col -= 1
        else:
            row += 1
            
    return False


if __name__ == "__main__":
    # Test Matrix Rotation
    mat1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    rotate_matrix_clockwise(mat1)
    assert mat1 == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]
    
    # Test Spiral Traversal
    mat2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    assert spiral_order(mat2) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    
    # Test Search 2D Matrix
    mat3 = [
        [1,  4,  7,  11],
        [2,  5,  8,  12],
        [3,  6,  9,  16],
        [10, 13, 14, 17]
    ]
    assert search_matrix_2d(mat3, 5) is True
    assert search_matrix_2d(mat3, 20) is False
    
    print("[SUCCESS] All Level 6 2D Matrix tests passed!")
