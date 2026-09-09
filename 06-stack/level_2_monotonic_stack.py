"""
Level 2: Monotonic Stack Patterns

Topics Covered:
1. Next Greater Element I O(N)
2. Daily Temperatures (Days until warmer temperature) O(N)

Monotonic Stack Invariant:
Maintain elements in strictly decreasing order.
When a larger element arrives, pop elements from stack until invariant is restored.
Each element is pushed and popped at most ONCE -> O(N) time!
"""

def next_greater_element(nums: list[int]) -> list[int]:
    """
    Finds the next greater element for each item in nums.
    Returns -1 if no greater element exists to the right.
    """
    result = [-1] * len(nums)
    stack = []  # Stores indices of elements
    
    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
        
    return result


def daily_temperatures(temperatures: list[int]) -> list[int]:
    """
    Finds number of days you have to wait after the i-th day to get a warmer temperature.
    Returns 0 if no future day is warmer.
    """
    result = [0] * len(temperatures)
    stack = []  # Stores indices of days
    
    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            prev_day = stack.pop()
            result[prev_day] = i - prev_day
        stack.append(i)
        
    return result


if __name__ == "__main__":
    # Test Next Greater Element
    assert next_greater_element([2, 1, 2, 4, 3]) == [4, 2, 4, -1, -1]
    
    # Test Daily Temperatures
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    
    print("[SUCCESS] All Level 2 Monotonic Stack tests passed!")
