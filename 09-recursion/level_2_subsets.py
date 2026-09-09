"""
Level 2: Decision Trees & Subsets Recursion

Topics Covered:
1. Power Set Generation (Include / Exclude Recursive Tree O(2^N))

Complexity:
- Time Complexity: O(2^N * N) where N is array length.
- Space Complexity: O(N) auxiliary recursion stack depth.
"""

def generate_subsets(nums: list[int]) -> list[list[int]]:
    """
    Generates all possible subsets (the power set) of an array of unique integers.
    Uses Include/Exclude recursive backtracking approach.
    """
    results = []
    
    def backtrack(index: int, current_subset: list[int]):
        if index == len(nums):
            results.append(list(current_subset))
            return
            
        # Option 1: Include nums[index]
        current_subset.append(nums[index])
        backtrack(index + 1, current_subset)
        
        # Backtrack: Undo inclusion
        current_subset.pop()
        
        # Option 2: Exclude nums[index]
        backtrack(index + 1, current_subset)
        
    backtrack(0, [])
    return results


if __name__ == "__main__":
    # Test Subsets Generation
    subsets = generate_subsets([1, 2, 3])
    assert len(subsets) == 8  # 2^3 = 8 subsets
    assert [] in subsets
    assert [1, 2, 3] in subsets
    
    print("[SUCCESS] All Level 2 Subsets Recursion tests passed!")
