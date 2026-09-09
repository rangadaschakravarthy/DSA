"""
Level 9: Data Stream as Disjoint Intervals

Problem:
Given a data stream input of non-negative integers a1, a2, ..., an, 
summarize the numbers seen so far as a list of disjoint intervals.
Implement SummaryRanges class:
- `addNum(val: int)` Adds integer val to stream.
- `getIntervals() -> list[list[int]]` Returns summary of current stream as sorted disjoint intervals.

Time Complexity: O(N) per addNum (or O(log N) with BST/Treemap)
Space Complexity: O(N)
"""

class SummaryRanges:
    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        new_interval = [value, value]
        res = []
        i = 0
        n = len(self.intervals)
        
        while i < n and self.intervals[i][1] + 1 < value:
            res.append(self.intervals[i])
            i += 1
            
        while i < n and self.intervals[i][0] <= value + 1:
            new_interval[0] = min(new_interval[0], self.intervals[i][0])
            new_interval[1] = max(new_interval[1], self.intervals[i][1])
            i += 1
            
        res.append(new_interval)
        
        while i < n:
            res.append(self.intervals[i])
            i += 1
            
        self.intervals = res

    def getIntervals(self) -> list[list[int]]:
        return self.intervals


if __name__ == "__main__":
    sr = SummaryRanges()
    sr.addNum(1)
    assert sr.getIntervals() == [[1, 1]]
    sr.addNum(3)
    assert sr.getIntervals() == [[1, 1], [3, 3]]
    sr.addNum(2)
    assert sr.getIntervals() == [[1, 3]]
    sr.addNum(7)
    assert sr.getIntervals() == [[1, 3], [7, 7]]
    sr.addNum(6)
    assert sr.getIntervals() == [[1, 3], [6, 7]]
    print("[PASS] Level 9 Data Stream as Disjoint Intervals tests passed!")
