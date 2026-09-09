"""
Level 3: Permutations II (Unique Permutations)

Problem:
Given a collection of numbers, nums, that might contain duplicates, 
return all possible unique permutations in any order.

Time Complexity: O(N * N!)
Space Complexity: O(N) recursion depth + visited tracking
"""

def permute_unique(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    used = [False] * len(nums)

    def backtrack(current_path):
        if len(current_path) == len(nums):
            result.append(list(current_path))
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            # Skip duplicates: if previous duplicate element hasn't been used yet
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            current_path.append(nums[i])
            backtrack(current_path)
            current_path.pop()
            used[i] = False

    backtrack([])
    return result


if __name__ == "__main__":
    res = permute_unique([1, 1, 2])
    assert len(res) == 3
    assert [1, 1, 2] in res
    assert [1, 2, 1] in res
    assert [2, 1, 1] in res
    print("[PASS] Level 3 Permutations II tests passed!")
