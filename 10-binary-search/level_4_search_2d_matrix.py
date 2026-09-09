"""
Level 4: Search a 2D Matrix

Problem:
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Time Complexity: O(log(M * N))
Space Complexity: O(1)
"""

def search_matrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
        
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        r, c = mid // n, mid % n
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return False


if __name__ == "__main__":
    mat = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert search_matrix(mat, 3) == True
    assert search_matrix(mat, 13) == False
    print("[PASS] Level 4 Search 2D Matrix tests passed!")
