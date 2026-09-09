# 06-Stack Module Curriculum & Problem Guide

---

## Level-1: Stack Fundamentals & Min Stack

### Problem 1: Valid Parentheses
- **Question**: Given a string `s` containing bracket characters, determine if the input string is valid.
- **Description / Explanation**: Match closing brackets with the most recently opened unclosed bracket (LIFO).
- **Approach & Logic**:
  - Push open brackets to stack. On closing bracket, pop and verify match.
- **Sample Input**: `s = "()[]{}"`
- **Sample Output**: `True`
- **Explanation**: All open brackets are matched in correct order.
- **Python Implementation**: [`level_1_stack_basics.py`](file:///c:/Users/chakr/Downloads/DSA/06-stack/level_1_stack_basics.py)

---

## Level-2: Monotonic Stack Patterns

### Problem 1: Next Greater Element & Daily Temperatures
- **Question**: Given `temperatures`, return array `answer` where `answer[i]` is number of days until warmer temperature.
- **Description / Explanation**: Use Monotonic Decreasing Stack of indices to find next greater element in $O(N)$ time.
- **Approach & Logic**:
  - Maintain stack of indices in decreasing temperature order. While current temp > stack top: pop & compute index diff.
- **Sample Input**: `temperatures = [73, 74, 75, 71, 69, 72, 76, 73]`
- **Sample Output**: `[1, 1, 4, 2, 1, 1, 0, 0]`
- **Explanation**: Day 0 (73) waits 1 day for 74. Day 2 (75) waits 4 days for 76.
- **Python Implementation**: [`level_2_monotonic_stack.py`](file:///c:/Users/chakr/Downloads/DSA/06-stack/level_2_monotonic_stack.py)

---

## Level-3: Histogram Optimization

### Problem 1: Largest Rectangle in Histogram
- **Question**: Find area of largest rectangle in a histogram in $O(N)$ time.
- **Description / Explanation**: Monotonic Increasing Stack of bar indices.
- **Approach & Logic**:
  - When encountering shorter bar, pop from stack. Popped bar is shortest in range. Width $= i - \text{stack}[-1] - 1$.
- **Sample Input**: `heights = [2, 1, 5, 6, 2, 3]`
- **Sample Output**: `10`
- **Explanation**: Bars 5 and 6 form rectangle of width 2 and area $5 \times 2 = 10$.
- **Python Implementation**: [`level_3_histogram.py`](file:///c:/Users/chakr/Downloads/DSA/06-stack/level_3_histogram.py)

---

## Level-4: Reverse Polish Notation Evaluation

### Problem 1: Evaluate Reverse Polish Notation
- **Question**: Evaluate arithmetic expression string in Reverse Polish Notation (Postfix) in $O(N)$ time.
- **Description / Explanation**: Evaluate postfix operator application using stack.
- **Approach & Logic**:
  - Push operands to stack. On operator: pop $b$ and $a$, compute $a \text{ op } b$, push result back.
- **Sample Input**: `tokens = ["2", "1", "+", "3", "*"]`
- **Sample Output**: `9`
- **Explanation**: $(2 + 1) * 3 = 9$.
- **Python Implementation**: [`level_4_eval_rpn.py`](file:///c:/Users/chakr/Downloads/DSA/06-stack/level_4_eval_rpn.py)

---

## Level-5: Nested Character Decoding Stack

### Problem 1: Decode String
- **Question**: Decode string formatted as `k[encoded_string]` in $O(N)$ time.
- **Description / Explanation**: Expand nested repeated string patterns.
- **Approach & Logic**:
  - Push `(curr_str, repeat_count)` onto stack when encountering `'['`. On `']'`, pop and multiply string.
- **Sample Input**: `s = "3[a2[c]]"`
- **Sample Output**: `"accaccacc"`
- **Explanation**: `2[c]` expands to `"cc"`. `3[acc]` expands to `"accaccacc"`.
- **Python Implementation**: [`level_5_decode_string.py`](file:///c:/Users/chakr/Downloads/DSA/06-stack/level_5_decode_string.py)

---

## Level-6: 2D Matrix Maximal Rectangle

### Problem 1: Maximal Rectangle in Binary Matrix
- **Question**: Find area of largest rectangle containing only `'1'`s in a 2D binary matrix in $O(M \cdot N)$ time.
- **Description / Explanation**: Convert each matrix row into histogram heights and run Monotonic Stack.
- **Approach & Logic**:
  - `heights[c] = heights[c] + 1` if cell is `'1'` else 0. Execute Histogram Stack for each row.
- **Sample Input**: 
  ```python
  matrix = [
      ["1","0","1","0","0"],
      ["1","0","1","1","1"],
      ["1","1","1","1","1"],
      ["1","0","0","1","0"]
  ]
  ```
- **Sample Output**: `6`
- **Explanation**: 2x3 rectangle of `'1'`s in rows 1-2 columns 2-4 has area 6.
- **Python Implementation**: [`level_6_maximal_rectangle.py`](file:///c:/Users/chakr/Downloads/DSA/06-stack/level_6_maximal_rectangle.py)

---

## Level-7: Greedy Monotonic Stack Digit Reduction

### Problem 1: Remove K Digits
- **Question**: Remove `k` digits from integer string `num` to form the smallest possible integer in $O(N)$ time.
- **Description / Explanation**: Greedily remove larger leading digits using Monotonic Increasing Stack.
- **Approach & Logic**:
  - While `stack` and `k > 0` and `stack[-1] > digit`: pop from stack and decrement `k`.
- **Sample Input**: `num = "1432219", k = 3`
- **Sample Output**: `"1219"`
- **Explanation**: Removing '4', '3', and '2' yields smallest number `"1219"`.
- **Python Implementation**: [`level_7_remove_k_digits.py`](file:///c:/Users/chakr/Downloads/DSA/06-stack/level_7_remove_k_digits.py)

---

## Level-8: Monotonic Stack Boundary Trapping

### Problem 1: Trapping Rain Water via Stack
- **Question**: Compute trapped rainwater using Monotonic Stack in $O(N)$ time and $O(N)$ space.
- **Description / Explanation**: Calculate horizontal water layers trapped between left and right height boundaries.
- **Approach & Logic**:
  - Monotonic Decreasing Stack. When encountering taller bar: pop bottom `mid`, calculate `bounded_height * bounded_width`.
- **Sample Input**: `height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]`
- **Sample Output**: `6`
- **Explanation**: Total 6 units of trapped water calculated horizontally.
- **Python Implementation**: [`level_8_trapping_rain_water_stack.py`](file:///c:/Users/chakr/Downloads/DSA/06-stack/level_8_trapping_rain_water_stack.py)

---

## Level-9: Full Expression Parser & Calculator

### Problem 1: Basic Calculator
- **Question**: Evaluate a mathematical expression string containing integers, `+`, `-`, `(`, `)`, and spaces in $O(N)$ time.
- **Description / Explanation**: Evaluate nested parenthesized sub-expressions with sign stack.
- **Approach & Logic**:
  - Maintain `res`, `num`, and `sign`. On `'('`: push `(res, sign)` to stack. On `')'`: pop and resolve sub-expression.
- **Sample Input**: `s = "(1+(4+5+2)-3)+(6+8)"`
- **Sample Output**: `23`
- **Explanation**: Inner expression $(4+5+2)=11$. Total sum $= (1+11-3) + 14 = 9 + 14 = 23$.
- **Python Implementation**: [`level_9_basic_calculator.py`](file:///c:/Users/chakr/Downloads/DSA/06-stack/level_9_basic_calculator.py)
