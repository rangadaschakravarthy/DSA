"""
Level 7: Matrix Exponentiation O(log N)

Topics Covered:
1. Fast N-th Fibonacci via 2x2 Matrix Multiplication O(log N)

Recurrence Matrix:
[ F(n+1)  F(n)   ] = [ 1  1 ]^n
[ F(n)    F(n-1) ]   [ 1  0 ]
"""

def multiply_2x2(a: list[list[int]], b: list[list[int]], mod: int) -> list[list[int]]:
    """Multiplies two 2x2 matrices under modulo."""
    c = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % mod
    return c


def matrix_power_2x2(mat: list[list[int]], exp: int, mod: int) -> list[list[int]]:
    """Computes mat^exp for a 2x2 matrix in O(log exp) time."""
    result = [[1, 0], [0, 1]]  # Identity 2x2 matrix
    base = mat
    
    while exp > 0:
        if exp % 2 == 1:
            result = multiply_2x2(result, base, mod)
        base = multiply_2x2(base, base, mod)
        exp //= 2
        
    return result


def fibonacci_matrix(n: int, mod: int = 10**9 + 7) -> int:
    """Calculates n-th Fibonacci number in O(log N) time using Matrix Exponentiation."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
        
    transformation = [[1, 1], [1, 0]]
    res_mat = matrix_power_2x2(transformation, n - 1, mod)
    return res_mat[0][0]


if __name__ == "__main__":
    MOD = 10**9 + 7
    # Test Matrix Exponentiation Fibonacci
    assert fibonacci_matrix(10, MOD) == 55
    assert fibonacci_matrix(50, MOD) == (12586269025 % MOD)
    
    print("[SUCCESS] All Level 7 Matrix Exponentiation tests passed!")
