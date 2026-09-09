"""
Level 2: Circular Circuit & Greedy Surplus Tracking

Topics Covered:
1. Gas Station (Complete Circuit O(N) time, O(1) space)

Greedy Property:
1. If sum(gas) < sum(cost), it's IMPOSSIBLE to complete the circuit -> return -1.
2. If starting at index A cannot reach index B (tank becomes negative at B), then NO index between A and B can reach B either!
   So, reset starting candidate to B + 1 and reset current tank surplus to 0.
"""

def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    """
    Finds starting gas station index to travel around circuit once clockwise.
    Returns -1 if impossible.
    """
    if sum(gas) < sum(cost):
        return -1
        
    start_index = 0
    current_tank = 0
    
    for i in range(len(gas)):
        current_tank += gas[i] - cost[i]
        # If current tank drops below 0, reset start candidate to i + 1
        if current_tank < 0:
            start_index = i + 1
            current_tank = 0
            
    return start_index


if __name__ == "__main__":
    # Test Gas Station
    gas1 = [1, 2, 3, 4, 5]
    cost1 = [3, 4, 5, 1, 2]
    assert can_complete_circuit(gas1, cost1) == 3
    
    gas2 = [2, 3, 4]
    cost2 = [3, 4, 3]
    assert can_complete_circuit(gas2, cost2) == -1
    
    print("[SUCCESS] All Level 2 Gas Station tests passed!")
