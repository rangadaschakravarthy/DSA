"""
Level 1: Permutations & State-Space Tree Exploration

Topics Covered:
1. Permutations Generation O(N * N!)

Backtracking Template:
1. Choose an element.
2. Explore recursively.
3. Undo choice (Backtrack).
"""

def permute(nums: list[int]) -> list[list[int]]:
    """
    Generates all possible permutations of an array of distinct integers.
    """
    results = []
    
    def backtrack(current_path: list[int], remaining_set: set[int]):
        if len(current_path) == len(nums):
            results.append(list(current_path))
            return
            
        for num in list(remaining_set):
            # Choose
            current_path.append(num)
            remaining_set.remove(num)
            
            # Explore
            backtrack(current_path, remaining_set)
            
            # Undo (Backtrack)
            remaining_set.add(num)
            current_path.pop()
            
    backtrack([], set(nums))
    return results


if __name__ == "__main__":
    # Test Permutations
    perms = permute([1, 2, 3])
    assert len(perms) == 6  # 3! = 6
    assert [1, 2, 3] in perms
    assert [3, 2, 1] in perms
    
    print("[SUCCESS] All Level 1 Permutations tests passed!")
