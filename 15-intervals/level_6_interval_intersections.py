"""
Level 6: Interval List Intersections

Problem:
You are given two lists of closed intervals, firstList and secondList, 
where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. 
Each list of intervals is pairwise disjoint and in sorted order.
Return the intersection of these two interval lists.

Time Complexity: O(N + M)
Space Complexity: O(N + M) output list
"""

def interval_intersection(firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
    i, j = 0, 0
    result = []
    
    while i < len(firstList) and j < len(secondList):
        start = max(firstList[i][0], secondList[j][0])
        end = min(firstList[i][1], secondList[j][1])
        
        if start <= end:
            result.append([start, end])
            
        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1
            
    return result


if __name__ == "__main__":
    l1 = [[0, 2], [5, 10], [13, 23], [24, 25]]
    l2 = [[1, 5], [8, 12], [15, 24], [25, 26]]
    expected = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    assert interval_intersection(l1, l2) == expected
    print("[PASS] Level 6 Interval List Intersections tests passed!")
