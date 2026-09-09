"""
Level 8: Expression Add Operators

Problem:
Given a string num that contains only digits and an integer target, 
return all possibilities to insert the binary operators '+', '-', and/or '*' 
between the digits of num so that the resultant expression evaluates to target.

Time Complexity: O(4^N)
Space Complexity: O(N) recursion stack
"""

def add_operators(num: str, target: int) -> list[str]:
    result = []
    
    def backtrack(idx, prev_operand, current_val, expression):
        if idx == len(num):
            if current_val == target:
                result.append(expression)
            return

        for i in range(idx + 1, len(num) + 1):
            sub_str = num[idx:i]
            # Avoid leading zeros in numbers longer than 1 digit
            if len(sub_str) > 1 and sub_str[0] == '0':
                continue
                
            val = int(sub_str)
            
            if idx == 0:
                # First number, pick it without operator
                backtrack(i, val, val, sub_str)
            else:
                # Addition
                backtrack(i, val, current_val + val, expression + "+" + sub_str)
                # Subtraction
                backtrack(i, -val, current_val - val, expression + "-" + sub_str)
                # Multiplication
                backtrack(i, prev_operand * val, current_val - prev_operand + (prev_operand * val), expression + "*" + sub_str)

    backtrack(0, 0, 0, "")
    return result


if __name__ == "__main__":
    res1 = add_operators("123", 6)
    assert "1+2+3" in res1
    assert "1*2*3" in res1
    
    res2 = add_operators("232", 8)
    assert "2*3+2" in res2
    assert "2+3*2" in res2
    
    print("[PASS] Level 8 Expression Add Operators tests passed!")
