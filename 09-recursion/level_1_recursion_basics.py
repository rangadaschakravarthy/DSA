"""
Level 1: Recursion Fundamentals & Call Stack

Topics Covered:
1. Recursive Base Cases & Recurrence Relations
2. Top-Down Memoization (Fibonacci / Climbing Stairs O(N))

Complexity:
- Time Complexity: O(N) with memoization (down from O(2^N)).
- Space Complexity: O(N) call stack + memo dictionary.
"""

def fibonacci_memo(n: int, memo: dict = None) -> int:
    """
    Calculates n-th Fibonacci number using top-down recursive memoization.
    """
    if memo is None:
        memo = {}
        
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    if n == 1:
        return 1
        
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


def climb_stairs(n: int) -> int:
    """
    Calculates number of distinct ways to climb n stairs taking 1 or 2 steps at a time.
    Relies on recurrence: ways(n) = ways(n - 1) + ways(n - 2).
    """
    memo = {}
    
    def solve(steps: int) -> int:
        if steps == 0:
            return 1
        if steps < 0:
            return 0
        if steps in memo:
            return memo[steps]
            
        memo[steps] = solve(steps - 1) + solve(steps - 2)
        return memo[steps]
        
    return solve(n)


if __name__ == "__main__":
    # Test Fibonacci
    assert fibonacci_memo(10) == 55
    assert fibonacci_memo(50) == 12586269025
    
    # Test Climbing Stairs
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(5) == 8
    
    print("[SUCCESS] All Level 1 Recursion tests passed!")
