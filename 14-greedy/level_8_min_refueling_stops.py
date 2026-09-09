"""
Level 8: Minimum Number of Refueling Stops

Problem:
A car travels from a starting position to a target destination. 
Initially, the car has startFuel liters of fuel. There are gas stations along the way.
Return the minimum number of refueling stops the car must make to reach target, or -1 if unreachable.

Time Complexity: O(N log N)
Space Complexity: O(N) max-heap
"""
import heapq

def min_refuel_stops(target: int, startFuel: int, stations: list[list[int]]) -> int:
    max_heap = []  # stores fuel capacity of passed stations
    stops = 0
    curr_fuel = startFuel
    i = 0
    n = len(stations)
    
    while curr_fuel < target:
        # Add all reachable stations to heap
        while i < n and stations[i][0] <= curr_fuel:
            heapq.heappush(max_heap, -stations[i][1])
            i += 1
            
        if not max_heap:
            return -1
            
        curr_fuel += -heapq.heappop(max_heap)
        stops += 1
        
    return stops


if __name__ == "__main__":
    assert min_refuel_stops(1, 1, []) == 0
    assert min_refuel_stops(100, 1, [[10, 100]]) == -1
    assert min_refuel_stops(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]) == 2
    print("[PASS] Level 8 Minimum Number of Refueling Stops tests passed!")
