"""
Level 5: Combination Sum

Problem:
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
The same number may be chosen from candidates an unlimited number of times.

Time Complexity: O(2^T) where T is target / min candidate value.
Space Complexity: O(T) recursion depth.
"""

def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    result = []
    
    def backtrack(start_idx, current_combination, current_sum):
        if current_sum == target:
            result.append(list(current_combination))
            return
        if current_sum > target:
            return
            
        for i in range(start_idx, len(candidates)):
            current_combination.append(candidates[i])
            backtrack(i, current_combination, current_sum + candidates[i])
            current_combination.pop()

    backtrack(0, [], 0)
    return result


if __name__ == "__main__":
    res = combination_sum([2, 3, 6, 7], 7)
    assert [2, 2, 3] in res
    assert [7] in res
    assert len(res) == 2
    print("[PASS] Level 5 Combination Sum tests passed!")
