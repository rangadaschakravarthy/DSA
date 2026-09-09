# Topic 9: Recursion & Backtracking Basics (Level 1 to Level 9)

Recursion is a programming technique where a function calls itself to break down a problem into smaller, identical subproblems until a base condition is met.

---

## Level-1: Recursion Basics & Factorial / Fibonacci

### Question
Implement recursive functions to calculate the factorial of $N$ and the $N$-th Fibonacci number.

### Description / Explanation
- Factorial $N! = N \times (N-1)!$ with base case $0! = 1$.
- Fibonacci $F(N) = F(N-1) + F(N-2)$ with base cases $F(0)=0, F(1)=1$.

### Logic / Approach
1. Define base cases first to prevent infinite call stacks.
2. Formulate state recurrence relation.

### Sample Input & Output
- **Input**: $N = 5$
- **Output**: Factorial = `120`, Fibonacci(5) = `5`

### Explanation
- $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$.
- Fibonacci sequence: $0, 1, 1, 2, 3, 5$.

### Python Implementation
- [`level_1_recursion_basics.py`](file:///c:/Users/chakr/Downloads/DSA/09-recursion/level_1_recursion_basics.py)

---

## Level-2: Generate All Subsets (Power Set)

### Question
Given an integer array `nums` of unique elements, return all possible subsets (the power set).

### Description / Explanation
Generate all $2^N$ combinations of elements.

### Logic / Approach
- At each element index, decide whether to include or exclude the element from current path.

### Sample Input & Output
- **Input**: `[1, 2]`
- **Output**: `[[], [1], [2], [1, 2]]`

### Explanation
2 choices per element $\rightarrow 2^2 = 4$ total subsets.

### Python Implementation
- [`level_2_subsets.py`](file:///c:/Users/chakr/Downloads/DSA/09-recursion/level_2_subsets.py)

---

## Level-3: Tower of Hanoi

### Question
Move $N$ disks from source rod A to target rod C using auxiliary rod B following puzzle rules.

### Description / Explanation
1. Move $N-1$ disks from A to B using C.
2. Move $N$-th disk from A to C.
3. Move $N-1$ disks from B to C using A.

### Logic / Approach
Recursive breakdown with state `(n, source, target, aux)`.

### Sample Input & Output
- **Input**: $N = 3$
- **Output**: 7 move sequence list `[('A', 'C'), ('A', 'B'), ..., ('A', 'C')]`

### Explanation
Total moves $= 2^N - 1 = 7$.

### Python Implementation
- [`level_3_tower_of_hanoi.py`](file:///c:/Users/chakr/Downloads/DSA/09-recursion/level_3_tower_of_hanoi.py)

---

## Level-4: Generate All Permutations

### Question
Given an array `nums` of distinct integers, return all possible permutations.

### Description / Explanation
Generate all $N!$ orderings of the array.

### Logic / Approach
Backtracking decision tree picking available numbers at each step.

### Sample Input & Output
- **Input**: `[1, 2, 3]`
- **Output**: `[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]`

### Explanation
3 choices for 1st pos, 2 for 2nd, 1 for 3rd $\rightarrow 3! = 6$.

### Python Implementation
- [`level_4_permutations.py`](file:///c:/Users/chakr/Downloads/DSA/09-recursion/level_4_permutations.py)

---

## Level-5: Combination Sum

### Question
Find all unique combinations of candidates summing to target where numbers can be reused unlimited times.

### Description / Explanation
Backtracking with state `(index, current_combo, current_sum)`.

### Logic / Approach
Pass current index `i` recursively to allow picking same element multiple times.

### Sample Input & Output
- **Input**: `candidates = [2, 3, 6, 7]`, `target = 7`
- **Output**: `[[2, 2, 3], [7]]`

### Explanation
$2+2+3=7$ and $7=7$.

### Python Implementation
- [`level_5_combination_sum.py`](file:///c:/Users/chakr/Downloads/DSA/09-recursion/level_5_combination_sum.py)

---

## Level-6: Decode String

### Question
Decode string encoded in pattern `k[encoded_string]`.

### Description / Explanation
Nested bracket expression evaluation using call stack / recursion.

### Logic / Approach
When encounter digit, build $k$. When `[`, recurse to evaluate sub-expression, multiply by $k$, and append.

### Sample Input & Output
- **Input**: `"3[a2[c]]"`
- **Output**: `"accaccacc"`

### Explanation
`2[c]` $\rightarrow$ `"cc"`. `a2[c]` $\rightarrow$ `"acc"`. `3[acc]` $\rightarrow$ `"accaccacc"`.

### Python Implementation
- [`level_6_decode_string.py`](file:///c:/Users/chakr/Downloads/DSA/09-recursion/level_6_decode_string.py)

---

## Level-7: K-th Symbol in Grammar

### Question
Start with 0. In each row, replace 0 with 01 and 1 with 10. Find $K$-th symbol in row $N$.

### Description / Explanation
Row $N$ has $2^{N-1}$ elements. First half is identical to row $N-1$, second half is bitwise inverse.

### Logic / Approach
If $K \le mid$, recurse `(N-1, K)`. If $K > mid$, return `1 - recurse(N-1, K - mid)`.

### Sample Input & Output
- **Input**: $N=3, K=3$
- **Output**: `1`

### Explanation
Row 1: `0`
Row 2: `01`
Row 3: `0110` $\rightarrow 3rd$ symbol is `1`.

### Python Implementation
- [`level_7_kth_symbol_grammar.py`](file:///c:/Users/chakr/Downloads/DSA/09-recursion/level_7_kth_symbol_grammar.py)

---

## Level-8: Expression Add Operators

### Question
Insert operators `+`, `-`, `*` between digits of string `num` to evaluate to `target`.

### Description / Explanation
Backtracking with state tracking previous operand for multiplication precedence.

### Logic / Approach
Maintain `prev_operand` to undo previous operation when handling `*`.

### Sample Input & Output
- **Input**: `num = "232"`, `target = 8`
- **Output**: `["2*3+2", "2+3*2"]`

### Explanation
$2 \times 3 + 2 = 8$ and $2 + 3 \times 2 = 8$.

### Python Implementation
- [`level_8_expression_add_operators.py`](file:///c:/Users/chakr/Downloads/DSA/09-recursion/level_8_expression_add_operators.py)

---

## Level-9: Parse Lisp Expression

### Question
Evaluate Lisp expression supporting `let`, `add`, `mult`, and nested scoping environments.

### Description / Explanation
Recursive AST parser and evaluator with environment dictionaries.

### Logic / Approach
Tokenize parenthesized expression, evaluate operators recursively passing current scope map.

### Sample Input & Output
- **Input**: `"(let x 2 (mult x (let x 3 y 4 (add x y))))"`
- **Output**: `14`

### Explanation
Inner `x=3, y=4` $\rightarrow add = 7$. Outer `x=2` $\rightarrow 2 \times 7 = 14$.

### Python Implementation
- [`level_9_parse_lisp_expression.py`](file:///c:/Users/chakr/Downloads/DSA/09-recursion/level_9_parse_lisp_expression.py)
