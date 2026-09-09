"""
Level 1: Queue Fundamentals & Two-Stack Queue Design

Topics Covered:
1. Implement FIFO Queue using two LIFO Stacks (in_stack & out_stack)

Complexity:
- Push: O(1)
- Pop / Peek: O(1) amortized
- Empty: O(1)
"""

class MyQueue:
    """
    Implements a First-In-First-Out (FIFO) queue using only two standard stacks.
    """
    
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        """Pushes element x to the back of queue."""
        self.in_stack.append(x)

    def _transfer(self) -> None:
        """Helper to transfer elements from in_stack to out_stack if out_stack is empty."""
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        """Removes element from front of queue and returns it."""
        self._transfer()
        return self.out_stack.pop()

    def peek(self) -> int:
        """Gets element at front of queue without removing it."""
        self._transfer()
        return self.out_stack[-1]

    def empty(self) -> bool:
        """Returns True if queue is empty."""
        return not self.in_stack and not self.out_stack


if __name__ == "__main__":
    # Test Queue implementation
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert q.empty() is False
    assert q.pop() == 2
    assert q.empty() is True
    
    print("[SUCCESS] All Level 1 Queue tests passed!")
