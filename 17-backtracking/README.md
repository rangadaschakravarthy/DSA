# Topic 17: Backtracking (Level 1 to Level 9)

Backtracking is a systematic method for exploring all configuration spaces by incrementally building candidates and undoing choices (backtracking) as soon as a constraint violation or terminal state is reached.

---

## Level-1: Subsets II (Handling Duplicate Elements)

### Question
Given an integer array `nums` that may contain duplicates, return all unique subsets.

### Description / Explanation
Prune duplicate subsets at the same tree depth level.

### Logic / Approach
Sort array. In loop, if `i > start_idx` and `nums[i] == nums[i-1]`, skip iteration.

### Sample Input & Output
- **Input**: `[1, 2, 2]`
- **Output**: `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`

### Explanation
6 unique subsets (no duplicate subsets generated).

### Python Implementation
- [`level_1_subsets_ii.py`](file:///c:/Users/chakr/Downloads/DSA/17-backtracking/level_1_subsets_ii.py)

---

## Level-2: Combination Sum II

### Question
Find all unique combinations summing to `target` where each number may be used only ONCE.

### Description / Explanation
Backtracking with deduplication.

### Logic / Approach
Sort array. Advance `start_idx` to `i + 1` in recursive call and skip duplicate consecutive values.

### Sample Input & Output
- **Input**: `candidates = [10, 1, 2, 7, 6, 1, 5]`, `target = 8`
- **Output**: `[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]`

### Explanation
Each combination sums to 8 and uses each array element at most once.

### Python Implementation
- [`level_2_combination_sum_ii.py`](file:///c:/Users/chakr/Downloads/DSA/17-backtracking/level_2_combination_sum_ii.py)

---

## Level-3: Permutations II (Unique Permutations)

### Question
Given a collection of numbers containing duplicates, return all unique permutations.

### Description / Explanation
Backtracking with a boolean `used` array.

### Logic / Approach
Sort numbers. Skip choice if `nums[i] == nums[i-1]` and `not used[i-1]`.

### Sample Input & Output
- **Input**: `[1, 1, 2]`
- **Output**: `[[1, 1, 2], [1, 2, 1], [2, 1, 1]]`

### Explanation
3 unique orderings.

### Python Implementation
- [`level_3_permutations_ii.py`](file:///c:/Users/chakr/Downloads/DSA/17-backtracking/level_3_permutations_ii.py)

---

## Level-4: Word Search I

### Question
Determine if a target `word` exists in an $M \times N$ character matrix by traversing adjacent cells.

### Description / Explanation
Grid DFS backtracking.

### Logic / Approach
Temporarily mark visited cell with `'#'`, recurse in 4 directions, then restore original character upon backtracking.

### Sample Input & Output
- **Input**: Board matrix, `word = "ABCCED"`
- **Output**: `True`

### Explanation
Found valid contiguous path matching string.

### Python Implementation
- [`level_4_word_search.py`](file:///c:/Users/chakr/Downloads/DSA/17-backtracking/level_4_word_search.py)

---

## Level-5: Palindrome Partitioning

### Question
Partition string `s` such that every substring is a palindrome.

### Description / Explanation
All-substring partitioning using palindrome validation.

### Logic / Approach
Branch recursively when prefix `s[start:end]` is a palindrome.

### Sample Input & Output
- **Input**: `"aab"`
- **Output**: `[["a", "a", "b"], ["aa", "b"]]`

### Explanation
Both partitions consist exclusively of palindrome substrings.

### Python Implementation
- [`level_5_palindrome_partitioning.py`](file:///c:/Users/chakr/Downloads/DSA/17-backtracking/level_5_palindrome_partitioning.py)

---

## Level-6: N-Queens Problem

### Question
Place $N$ non-attacking queens on an $N \times N$ chessboard.

### Description / Explanation
Constraint propagation using sets tracking columns and diagonal conflicts.

### Logic / Approach
Track `cols`, `pos_diag (r + c)`, and `neg_diag (r - c)`. Try placing queen at each column in current row $R$.

### Sample Input & Output
- **Input**: $N = 4$
- **Output**: 2 distinct 4x4 board arrangements.

### Explanation
Queens placed so no two share same row, column, or diagonal.

### Python Implementation
- [`level_6_n_queens.py`](file:///c:/Users/chakr/Downloads/DSA/17-backtracking/level_6_n_queens.py)

---

## Level-7: Sudoku Solver

### Question
Solve a 9x9 Sudoku grid by filling empty cells `'.'`.

### Description / Explanation
Exact Cover Backtracking.

### Logic / Approach
Find empty cell, try digits 1-9, check validity (row, col, 3x3 box), recurse. If dead end, backtrack cell to `'.'`.

### Sample Input & Output
- **Input**: 9x9 partial Sudoku board
- **Output**: Fully solved 9x9 Sudoku board

### Explanation
Fills all 81 cells satisfying Sudoku rules.

### Python Implementation
- [`level_7_sudoku_solver.py`](file:///c:/Users/chakr/Downloads/DSA/17-backtracking/level_7_sudoku_solver.py)

---

## Level-8: Word Search II (Trie + Backtracking)

### Question
Find all dictionary words present on a 2D character board.

### Description / Explanation
Multi-word grid search optimizing prefix matching via a Trie data structure.

### Logic / Approach
Store all dictionary words in a Trie. Run grid DFS checking child node existence in Trie, pruning leaf nodes when words are found.

### Sample Input & Output
- **Input**: Board matrix, `words = ["oath", "pea", "eat", "rain"]`
- **Output**: `["oath", "eat"]`

### Explanation
"oath" and "eat" exist on board; "pea" and "rain" do not.

### Python Implementation
- [`level_8_word_search_ii_trie.py`](file:///c:/Users/chakr/Downloads/DSA/17-backtracking/level_8_word_search_ii_trie.py)

---

## Level-9: Robot Room Cleaner

### Question
Clean an unknown room layout using a robot API supporting `move()`, `turnLeft()`, `turnRight()`, and `clean()`.

### Description / Explanation
Autonomous exploration via Spiral Backtracking DFS.

### Logic / Approach
Track visited coordinates `(r, c)`. For each unvisited cell, clean, recurse forward, and issue reverse backtrack sequence (`turnRight() * 2 -> move() -> turnRight() * 2`).

### Sample Input & Output
- **Input**: Room grid with obstacles, start `(0, 0)`
- **Output**: All 10 accessible cells cleaned.

### Explanation
Robot explores and cleans every reachable room cell before returning to start position.

### Python Implementation
- [`level_9_robot_room_cleaner.py`](file:///c:/Users/chakr/Downloads/DSA/17-backtracking/level_9_robot_room_cleaner.py)
