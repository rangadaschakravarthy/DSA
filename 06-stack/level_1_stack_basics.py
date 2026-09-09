"""
Level 1: Stack Fundamentals & Min Stack Design

Topics Covered:
1. Valid Parentheses Matching O(N)
2. Min Stack Design O(1) time for push, pop, top, getMin

Complexity:
- Valid Parentheses: O(N) time, O(N) space.
- Min Stack: O(1) time per operation, O(N) space for auxiliary min tracking.
"""

def is_valid_parentheses(s: str) -> bool:
    """
    Determines if input string containing brackets '()[]{}' is valid.
    """
    matching = {')': '(', ']': '[', '}': '{'}
    stack = []
    
    for char in s:
        if char in matching:
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
            
    return len(stack) == 0


class MinStack:
    """
    Stack design that supports push, pop, top, and retrieving the minimum element in O(1) time.
    """
    
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push to min_stack if it's <= current minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else -1

    def get_min(self) -> int:
        return self.min_stack[-1] if self.min_stack else -1


if __name__ == "__main__":
    # Test Valid Parentheses
    assert is_valid_parentheses("()") is True
    assert is_valid_parentheses("()[]{}") is True
    assert is_valid_parentheses("(]") is False
    assert is_valid_parentheses("([)]") is False
    
    # Test Min Stack
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert min_stack.get_min() == -3
    min_stack.pop()
    assert min_stack.top() == 0
    assert min_stack.get_min() == -2
    
    print("[SUCCESS] All Level 1 Stack Basics tests passed!")
