"""
Level 7: Greedy Monotonic Stack Digit Reduction

Topics Covered:
1. Remove K Digits to form smallest possible integer O(N) time, O(N) space

Algorithm:
Maintain a Monotonic Increasing Stack of digits.
If current digit < stack top, pop stack top and decrement k (greedily remove larger leading digits!).
"""

def remove_kdigits(num: str, k: int) -> str:
    """
    Removes k digits from non-negative integer string num to form the smallest possible integer.
    """
    stack = []
    
    for digit in num:
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
        
    # If k > 0 remains, pop remaining digits from end
    if k > 0:
        stack = stack[:-k]
        
    # Strip leading zeros
    result = "".join(stack).lstrip('0')
    return result if result else "0"


if __name__ == "__main__":
    assert remove_kdigits("1432219", 3) == "1219"
    assert remove_kdigits("10200", 1) == "200"
    assert remove_kdigits("10", 2) == "0"
    
    print("[SUCCESS] All Level 7 Remove K Digits tests passed!")
