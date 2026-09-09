"""
Level 2: Combination Sum & Target Pruning

Topics Covered:
1. Combination Sum (Unlimited usage of candidates)

Pruning Optimization:
Sort candidates array to stop exploring as soon as candidate > remaining target!
"""

def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    """
    Finds all unique combinations in candidates where chosen numbers sum to target.
    Same number may be chosen unlimited times.
    """
    candidates.sort()
    results = []
    
    def backtrack(start_idx: int, remaining_target: int, current_path: list[int]):
        if remaining_target == 0:
            results.append(list(current_path))
            return
            
        for i in range(start_idx, len(candidates)):
            cand = candidates[i]
            if cand > remaining_target:
                break  # Prune branch since array is sorted!
                
            current_path.append(cand)
            # Pass i (not i + 1) because same element can be reused
            backtrack(i, remaining_target - cand, current_path)
            current_path.pop()
            
    backtrack(0, target, [])
    return results


if __name__ == "__main__":
    # Test Combination Sum
    assert combination_sum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert combination_sum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    
    print("[SUCCESS] All Level 2 Combination Sum tests passed!")
