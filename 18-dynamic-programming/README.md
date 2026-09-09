# Topic 18: Dynamic Programming (Level 1 to Level 9)

Dynamic Programming (DP) optimizes recursive algorithms with overlapping subproblems and optimal substructure by memoizing (top-down) or tabulating (bottom-up) subproblem results.

---

## Level-1: Climbing Stairs & Min Cost Climbing Stairs

### Question
1. Find distinct ways to climb $N$ stairs taking 1 or 2 steps.
2. Find minimum cost to reach top paying `cost[i]` per step.

### Description / Explanation
$F(N) = F(N-1) + F(N-2)$ recurrence.

### Logic / Approach
State compression using 2 variables `prev2` and `prev1` in $O(1)$ space.

### Sample Input & Output
- **Input**: $N = 5$, `cost = [10, 15, 20]`
- **Output**: `climb_stairs = 8`, `min_cost = 15`

### Explanation
8 distinct paths; minimum cost is 15 starting from index 1.

### Python Implementation
- [`level_1_climbing_stairs.py`](file:///c:/Users/chakr/Downloads/DSA/18-dynamic-programming/level_1_climbing_stairs.py)

---

## Level-2: House Robber I & II

### Question
1. Maximize money robbed without robbing adjacent houses.
2. Houses arranged in a circle.

### Description / Explanation
`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`.

### Logic / Approach
For circular arrangement, run linear house robber twice: once excluding first house `nums[:-1]`, once excluding last house `nums[1:]`.

### Sample Input & Output
- **Input**: Linear `[2, 7, 9, 3, 1]`, Circular `[2, 3, 2]`
- **Output**: Linear `12`, Circular `3`

### Explanation
Linear: rob 2, 9, 1 (total 12). Circular: rob house 1 (3).

### Python Implementation
- [`level_2_house_robber.py`](file:///c:/Users/chakr/Downloads/DSA/18-dynamic-programming/level_2_house_robber.py)

---

## Level-3: Coin Change & Target Sum

### Question
1. Find fewest coins needed to total `amount`.
2. Find ways to assign $+/-$ signs to achieve target sum.

### Description / Explanation
Unbounded Knapsack & Subset Sum transformation.

### Logic / Approach
- Coin Change: `dp[i] = min(dp[i], dp[i - coin] + 1)`.
- Target Sum: transform to Subset Sum target $P = (\text{total} + \text{target}) / 2$.

### Sample Input & Output
- **Input**: `coins = [1, 2, 5]`, `amount = 11`
- **Output**: `3`

### Explanation
$5 + 5 + 1 = 11$ (3 coins).

### Python Implementation
- [`level_3_coin_change.py`](file:///c:/Users/chakr/Downloads/DSA/18-dynamic-programming/level_3_coin_change.py)

---

## Level-4: Longest Increasing Subsequence (LIS)

### Question
Find length of longest strictly increasing subsequence.

### Description / Explanation
Binary search tail array optimization.

### Logic / Approach
Maintain `tails` array. Use `bisect_left` to replace smallest tail element $\ge num$, or append if $num >$ all tails.

### Sample Input & Output
- **Input**: `[10, 9, 2, 5, 3, 7, 101, 18]`
- **Output**: `4`

### Explanation
Longest increasing subsequence `[2, 3, 7, 101]` (length 4).

### Python Implementation
- [`level_4_longest_increasing_subsequence.py`](file:///c:/Users/chakr/Downloads/DSA/18-dynamic-programming/level_4_longest_increasing_subsequence.py)

---

## Level-5: LCS & Edit Distance

### Question
1. Longest Common Subsequence of two strings.
2. Minimum operations (insert, delete, replace) to convert string 1 to string 2.

### Description / Explanation
2D Grid DP matching character transitions.

### Logic / Approach
- LCS: `dp[i][j] = dp[i-1][j-1] + 1` if match, else `max(dp[i-1][j], dp[i][j-1])`.
- Edit Distance: `1 + min(insert, delete, replace)`.

### Sample Input & Output
- **Input**: `s1 = "horse"`, `s2 = "ros"`
- **Output**: `3`

### Explanation
Replace 'h' with 'r', remove 'r', remove 'e' (3 operations).

### Python Implementation
- [`level_5_lcs_edit_distance.py`](file:///c:/Users/chakr/Downloads/DSA/18-dynamic-programming/level_5_lcs_edit_distance.py)

---

## Level-6: 0/1 Knapsack & Partition Equal Subset Sum

### Question
1. Maximize item value within capacity $W$.
2. Check if array can be split into two subsets with equal sum.

### Description / Explanation
0/1 Knapsack with 1D backward loop space optimization.

### Logic / Approach
`dp[w] = max(dp[w], dp[w - weight[i]] + value[i])` iterating backwards from $W$ down to `weight[i]`.

### Sample Input & Output
- **Input**: `nums = [1, 5, 11, 5]`
- **Output**: `True`

### Explanation
Partition `[1, 5, 5]` and `[11]` both sum to 11.

### Python Implementation
- [`level_6_01_knapsack.py`](file:///c:/Users/chakr/Downloads/DSA/18-dynamic-programming/level_6_01_knapsack.py)

---

## Level-7: Word Break I & II

### Question
1. Check if string $S$ can be segmented into dictionary words.
2. Return all valid sentence segmentations.

### Description / Explanation
String segmentation with boolean DP table and Memoized DFS.

### Logic / Approach
`dp[i] = True` if `dp[j] == True` and `s[j:i]` is in dictionary.

### Sample Input & Output
- **Input**: `s = "leetcode"`, `wordDict = ["leet", "code"]`
- **Output**: `True`

### Explanation
Segmented as `"leet code"`.

### Python Implementation
- [`level_7_word_break.py`](file:///c:/Users/chakr/Downloads/DSA/18-dynamic-programming/level_7_word_break.py)

---

## Level-8: Maximal Rectangle in Binary Matrix

### Question
Find largest rectangle area containing only `'1'`s in a 2D binary grid.

### Description / Explanation
Histogram heights conversion + Monotonic Stack.

### Logic / Approach
Build 1D histogram height array per row. Run Largest Rectangle in Histogram algorithm using monotonic stack.

### Sample Input & Output
- **Input**: 4x5 binary matrix
- **Output**: `6`

### Explanation
Largest 1s rectangle has height 2 and width 3 (area 6).

### Python Implementation
- [`level_8_maximal_rectangle.py`](file:///c:/Users/chakr/Downloads/DSA/18-dynamic-programming/level_8_maximal_rectangle.py)

---

## Level-9: Burst Balloons (Interval DP)

### Question
Find max coins collected by bursting balloons where coin gain for balloon $K$ is `arr[left] * arr[k] * arr[right]`.

### Description / Explanation
Interval DP thinking backwards (last balloon to burst in range `[left, right]`).

### Logic / Approach
`dp[left][right] = max(dp[left][right], arr[left]*arr[k]*arr[right] + dp[left][k] + dp[k][right])`.

### Sample Input & Output
- **Input**: `[3, 1, 5, 8]`
- **Output**: `167`

### Explanation
Optimal burst sequence: $1 \rightarrow 5 \rightarrow 3 \rightarrow 8$ yielding 167 total coins.

### Python Implementation
- [`level_9_burst_balloons.py`](file:///c:/Users/chakr/Downloads/DSA/18-dynamic-programming/level_9_burst_balloons.py)
