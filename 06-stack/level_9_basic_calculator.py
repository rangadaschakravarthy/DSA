"""
Level 9: Full Expression Parser & Calculator Stack (Mastery Level)

Topics Covered:
1. Basic Calculator with '+', '-', parentheses '()', and spaces O(N) time, O(N) space

Logic:
Maintain current result and current sign (+1 or -1).
On '(', push (result, sign) to stack and reset. On ')', pop (prev_result, prev_sign) and combine!
"""

def calculate(s: str) -> int:
    """
    Evaluates a basic mathematical expression string containing non-negative integers, '+', '-', '(', ')', and spaces.
    """
    stack = []
    res = 0
    num = 0
    sign = 1  # 1 for '+', -1 for '-'
    
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '+':
            res += sign * num
            num = 0
            sign = 1
        elif char == '-':
            res += sign * num
            num = 0
            sign = -1
        elif char == '(':
            # Save current result and sign onto stack
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
        elif char == ')':
            res += sign * num
            num = 0
            prev_sign = stack.pop()
            prev_res = stack.pop()
            res = prev_res + prev_sign * res
            
    res += sign * num
    return res


if __name__ == "__main__":
    assert calculate("1 + 1") == 2
    assert calculate(" 2-1 + 2 ") == 3
    assert calculate("(1+(4+5+2)-3)+(6+8)") == 23
    
    print("[SUCCESS] All Level 9 Basic Calculator Mastery tests passed!")
