"""
Level 3: K Closest Points to Origin

Problem:
Given an array of points where points[i] = [xi, yi] and an integer k, return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance sqrt((x1 - x2)^2 + (y1 - y2)^2).

Time Complexity: O(N log K)
Space Complexity: O(K) max-heap
"""
import heapq

def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    # Use max-heap storing (-dist, x, y) to keep K smallest distances
    max_heap = []
    for x, y in points:
        dist = x * x + y * y
        heapq.heappush(max_heap, (-dist, x, y))
        if len(max_heap) > k:
            heapq.heappop(max_heap)
            
    return [[x, y] for _, x, y in max_heap]


if __name__ == "__main__":
    pts = [[1, 3], [-2, 2]]
    res = k_closest(pts, 1)
    assert res == [[-2, 2]]
    
    pts2 = [[3, 3], [5, -1], [-2, 4]]
    res2 = k_closest(pts2, 2)
    assert len(res2) == 2
    assert [3, 3] in res2 and [-2, 4] in res2
    print("[PASS] Level 3 K Closest Points to Origin tests passed!")
