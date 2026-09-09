"""
Level 7: Minimum Number of Arrows to Burst Balloons

Problem:
There are spherical balloons taped to a flat wall. 
Given points array where points[i] = [xstart, xend], return the minimum number of arrows to burst all balloons.

Time Complexity: O(N log N)
Space Complexity: O(1)
"""

def find_min_arrow_shots(points: list[list[int]]) -> int:
    if not points:
        return 0
        
    points.sort(key=lambda x: x[1])
    arrows = 1
    prev_end = points[0][1]
    
    for start, end in points[1:]:
        if start > prev_end:
            arrows += 1
            prev_end = end
            
    return arrows


if __name__ == "__main__":
    assert find_min_arrow_shots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
    assert find_min_arrow_shots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
    print("[PASS] Level 7 Minimum Number of Arrows to Burst Balloons tests passed!")
