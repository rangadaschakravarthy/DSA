"""
Level 3: Gas Station

Problem:
There are n gas stations along a circular route. Return the starting gas station's index 
if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Time Complexity: O(N)
Space Complexity: O(1)
"""

def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    if sum(gas) < sum(cost):
        return -1
        
    start_idx = 0
    current_tank = 0
    
    for i in range(len(gas)):
        current_tank += gas[i] - cost[i]
        if current_tank < 0:
            start_idx = i + 1
            current_tank = 0
            
    return start_idx


if __name__ == "__main__":
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    assert can_complete_circuit(gas, cost) == 3
    
    gas2 = [2, 3, 4]
    cost2 = [3, 4, 3]
    assert can_complete_circuit(gas2, cost2) == -1
    print("[PASS] Level 3 Gas Station tests passed!")
