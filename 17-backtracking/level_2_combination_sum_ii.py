"""
Level 2: Combination Sum II

Problem:
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target. 
Each number in candidates may only be used ONCE in the combination.

Time Complexity: O(2^N)
Space Complexity: O(N) recursion stack
"""

def combination_sum_2(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()
    result = []

    def backtrack(start_idx, current_path, current_sum):
        if current_sum == target:
            result.append(list(current_path))
            return
        if current_sum > target:
            return

        for i in range(start_idx, len(candidates)):
            if i > start_idx and candidates[i] == candidates[i - 1]:
                continue
            current_path.append(candidates[i])
            backtrack(i + 1, current_path, current_sum + candidates[i])
            current_path.pop()

    backtrack(0, [], 0)
    return result


if __name__ == "__main__":
    res = combination_sum_2([10, 1, 2, 7, 6, 1, 5], 8)
    assert [1, 1, 6] in res
    assert [1, 2, 5] in res
    assert [1, 7] in res
    assert [2, 6] in res
    assert len(res) == 4
    print("[PASS] Level 2 Combination Sum II tests passed!")
