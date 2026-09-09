"""
Level 4: Expression Evaluation & Reverse Polish Notation

Topics Covered:
1. Evaluate Reverse Polish Notation (RPN Postfix Expression O(N) time, O(N) space)

Complexity:
- Time Complexity: O(N) single pass.
- Space Complexity: O(N) stack size.
"""

def eval_rpn(tokens: list[str]) -> int:
    """
    Evaluates arithmetic expression in Reverse Polish Notation (Postfix).
    Valid operators are '+', '-', '*', '/'.
    """
    stack = []
    
    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                # Truncate towards zero integer division
                stack.append(int(a / b))
        else:
            stack.append(int(token))
            
    return stack[0]


if __name__ == "__main__":
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9  # (2 + 1) * 3 = 9
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6  # 4 + (13 // 5) = 6
    assert eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    
    print("[SUCCESS] All Level 4 Eval RPN tests passed!")
