"""
Level 1: Subsets II (Handling Duplicate Elements)

Problem:
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets.

Time Complexity: O(N * 2^N)
Space Complexity: O(N) recursion stack depth
"""

def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []

    def backtrack(start_idx, current_path):
        result.append(list(current_path))
        
        for i in range(start_idx, len(nums)):
            # Skip duplicates at the same tree level
            if i > start_idx and nums[i] == nums[i - 1]:
                continue
            current_path.append(nums[i])
            backtrack(i + 1, current_path)
            current_path.pop()

    backtrack(0, [])
    return result


if __name__ == "__main__":
    res = subsets_with_dup([1, 2, 2])
    assert len(res) == 6
    assert [] in res and [1] in res and [2] in res
    assert [1, 2] in res and [2, 2] in res and [1, 2, 2] in res
    print("[PASS] Level 1 Subsets II tests passed!")
