# 📝 Post-Mortem Mistake Log

Use this document to log every bug, logic error, or incorrect pattern choice. Learning from your mistakes is the fastest path to DSA mastery.

---

## 🛑 Taxonomy of Common DSA Mistakes

Before filling out your log, check if your bug falls into one of these classic categories:

1. **Off-by-One Errors**: `range(len(nums))` vs `range(len(nums) - 1)` or `low <= high` vs `low < high`.
2. **Variable State Leakage**: Forgetting to re-initialize containers or accumulators inside loops.
3. **Out-of-Bounds Indexing**: Dereferencing `nums[i + 1]` without bounds checks (`i < len(nums) - 1`).
4. **Incorrect Base Case**: Omitted or misordered base cases in recursive / DP solutions causing stack overflows.
5. **Modifying Collection While Iterating**: Deleting items from a `list` or `dict` while traversing it.
6. **Implicit Python Copying**: Passing mutable lists by reference (`path` vs `path[:]` in backtracking).
7. **Flawed Greedy Assumption**: Assuming locally optimal choice works without an exchange argument proof.
8. **Integer Floor Division Pitfall**: Negative integer division in Python (`-3 // 2 == -2`, not `-1`).

---

## 📓 Personal Mistake Entry Template

Copy and paste this template whenever a problem submission fails:

```markdown
### [Problem Name / ID] — Date: YYYY-MM-DD

- **Problem File**: [`path/to/problem.py`](file:///path/to/problem.py)
- **Primary Topic**: [e.g. Sliding Window]
- **What I Tried Initially**:
  - [Briefly describe your first approach and complexity]
- **Where I Got Stuck / What Broke**:
  - [e.g. Failed test case with negative numbers, Time Limit Exceeded, Index Error]
- **Root Cause & Correct Pattern**:
  - [Explain the exact flaw in reasoning and the correct pattern needed]
- **Key Insight to Remember**:
  - [One-sentence rule to prevent this mistake in the future]
- **Reattempt Scheduled Date**: [YYYY-MM-DD]
```

---

## 📜 Active Mistake Log Entries

### Entry 1 — Example Reference Entry
- **Problem File**: [`01-arrays/level-3/03_maximum_subarray_kadane.py`](file:///c:/Users/chakr/Downloads/DSA/01-arrays/level-3/03_maximum_subarray_kadane.py)
- **Primary Topic**: Arrays
- **What I Tried Initially**: Initialized `max_sum = 0`.
- **Where I Got Stuck**: Failed test case where all array elements were negative (`nums = [-5, -2, -9]`). Output was `0` instead of `-2`.
- **Root Cause & Correct Pattern**: Initializing max tracking variable to `0` fails when all numbers are negative.
- **Key Insight to Remember**: Always initialize max tracking variables to `nums[0]` or `-float('inf')`.
- **Reattempt Status**: Solved.
