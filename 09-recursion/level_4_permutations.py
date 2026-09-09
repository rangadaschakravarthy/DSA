"""
Level 4: Generate All Permutations

Problem:
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

Time Complexity: O(N * N!)
Space Complexity: O(N!) output space, O(N) recursion stack
"""

def permute(nums: list[int]) -> list[list[int]]:
    result = []
    
    def backtrack(path, remaining):
        if not remaining:
            result.append(list(path))
            return
        
        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i+1:])
            path.pop()

    backtrack([], nums)
    return result


if __name__ == "__main__":
    res = permute([1, 2, 3])
    assert len(res) == 6
    assert [1, 2, 3] in res
    assert [3, 2, 1] in res
    print("[PASS] Level 4 Permutations tests passed!")
