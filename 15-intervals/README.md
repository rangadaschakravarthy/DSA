# Topic 15: Intervals (Level 1 to Level 9)

Interval problems involve processing continuous continuous ranges `[start, end]`. Sorting intervals by start time or end time is usually the first key step.

---

## Level-1: Meeting Rooms I (Can Attend All Meetings)

### Question
Given meeting time intervals `[[s1,e1],[s2,e2],...]`, determine if a person could attend all meetings.

### Description / Explanation
Check for any overlapping adjacent meetings.

### Logic / Approach
Sort intervals by start time; return `False` if `intervals[i][1] > intervals[i+1][0]`.

### Sample Input & Output
- **Input**: `[[0, 30], [5, 10], [15, 20]]`
- **Output**: `False`

### Explanation
Meeting `[0, 30]` overlaps with `[5, 10]`.

### Python Implementation
- [`level_1_meeting_rooms_i.py`](file:///c:/Users/chakr/Downloads/DSA/15-intervals/level_1_meeting_rooms_i.py)

---

## Level-2: Merge Intervals

### Question
Merge all overlapping intervals and return non-overlapping intervals.

### Description / Explanation
Combine overlapping continuous time ranges.

### Logic / Approach
Sort by start time. If `current[0] <= prev[1]`, merge by setting `prev[1] = max(prev[1], current[1])`.

### Sample Input & Output
- **Input**: `[[1, 3], [2, 6], [8, 10], [15, 18]]`
- **Output**: `[[1, 6], [8, 10], [15, 18]]`

### Explanation
`[1, 3]` and `[2, 6]` merge into `[1, 6]`.

### Python Implementation
- [`level_2_merge_intervals.py`](file:///c:/Users/chakr/Downloads/DSA/15-intervals/level_2_merge_intervals.py)

---

## Level-3: Insert Interval

### Question
Insert `newInterval` into sorted non-overlapping intervals and merge if necessary.

### Description / Explanation
Single linear sweep inserting and merging on-the-fly.

### Logic / Approach
1. Add intervals ending before `newInterval` start.
2. Merge overlapping intervals into `newInterval`.
3. Add remaining intervals.

### Sample Input & Output
- **Input**: `intervals = [[1,3],[6,9]]`, `newInterval = [2,5]`
- **Output**: `[[1, 5], [6, 9]]`

### Explanation
`[2, 5]` merges with `[1, 3]` to become `[1, 5]`.

### Python Implementation
- [`level_3_insert_interval.py`](file:///c:/Users/chakr/Downloads/DSA/15-intervals/level_3_insert_interval.py)

---

## Level-4: Meeting Rooms II (Minimum Rooms Required)

### Question
Find minimum number of conference rooms required for meetings.

### Description / Explanation
Track concurrent meetings using Min-Heap of meeting end times.

### Logic / Approach
Sort by start time. Reuse room (pop top of Min-Heap) if earliest ending meeting ends $\le$ current start time.

### Sample Input & Output
- **Input**: `[[0, 30], [5, 10], [15, 20]]`
- **Output**: `2`

### Explanation
Room 1: `[0, 30]`, Room 2: `[5, 10]` then `[15, 20]`.

### Python Implementation
- [`level_4_meeting_rooms_ii.py`](file:///c:/Users/chakr/Downloads/DSA/15-intervals/level_4_meeting_rooms_ii.py)

---

## Level-5: Non-overlapping Intervals

### Question
Find minimum number of intervals to remove to make the remaining intervals non-overlapping.

### Description / Explanation
Greedy interval scheduling problem.

### Logic / Approach
Sort intervals by end time. Keep interval with earliest end time; remove overlapping intervals.

### Sample Input & Output
- **Input**: `[[1, 2], [2, 3], [3, 4], [1, 3]]`
- **Output**: `1`

### Explanation
Removing `[1, 3]` leaves non-overlapping intervals `[[1,2], [2,3], [3,4]]`.

### Python Implementation
- [`level_5_non_overlapping_intervals.py`](file:///c:/Users/chakr/Downloads/DSA/15-intervals/level_5_non_overlapping_intervals.py)

---

## Level-6: Interval List Intersections

### Question
Find intersection of two pairwise disjoint sorted interval lists.

### Description / Explanation
Two-pointer sweep over sorted interval lists.

### Logic / Approach
Overlap start is `max(l1[i][0], l2[j][0])`, overlap end is `min(l1[i][1], l2[j][1])`. Advance pointer with smaller end time.

### Sample Input & Output
- **Input**: `l1 = [[0,2],[5,10]]`, `l2 = [[1,5],[8,12]]`
- **Output**: `[[1, 2], [5, 5], [8, 10]]`

### Explanation
Intersections: `[0,2]` & `[1,5]` $\rightarrow [1,2]$; `[5,10]` & `[1,5]` $\rightarrow [5,5]$; `[5,10]` & `[8,12]` $\rightarrow [8,10]$.

### Python Implementation
- [`level_6_interval_intersections.py`](file:///c:/Users/chakr/Downloads/DSA/15-intervals/level_6_interval_intersections.py)

---

## Level-7: Minimum Number of Arrows to Burst Balloons

### Question
Find minimum arrows needed to burst all spherical balloons `[xstart, xend]`.

### Description / Explanation
Greedy activity selection variant.

### Logic / Approach
Sort by end coordinate `xend`. Shoot arrow at `prev_end`; count new arrow when next balloon starts $> prev\_end$.

### Sample Input & Output
- **Input**: `[[10, 16], [2, 8], [1, 6], [7, 12]]`
- **Output**: `2`

### Explanation
Arrow 1 at $x=6$ bursts `[1,6]` & `[2,8]`. Arrow 2 at $x=12$ bursts `[7,12]` & `[10,16]`.

### Python Implementation
- [`level_7_min_arrows_balloons.py`](file:///c:/Users/chakr/Downloads/DSA/15-intervals/level_7_min_arrows_balloons.py)

---

## Level-8: Employee Free Time

### Question
Find positive-length common free time intervals for all employees.

### Description / Explanation
Merge all working intervals, then gaps between merged intervals form free time.

### Logic / Approach
Flatten all intervals, sort by start time, merge overlapping working periods, then find gaps `[merged[i-1][1], merged[i][0]]`.

### Sample Input & Output
- **Input**: `schedule = [[[1,2],[5,6]], [[1,3]], [[4,10]]]`
- **Output**: `[[3, 4]]`

### Explanation
Working time merged is `[1, 3]` and `[4, 10]`. Common free time is `[3, 4]`.

### Python Implementation
- [`level_8_employee_free_time.py`](file:///c:/Users/chakr/Downloads/DSA/15-intervals/level_8_employee_free_time.py)

---

## Level-9: Data Stream as Disjoint Intervals

### Question
Maintain disjoint intervals summarizing integers added to data stream.

### Description / Explanation
Dynamic interval insertion and coalescing.

### Logic / Approach
When adding `val`, merge with existing intervals where `intervals[i][0] <= val + 1` and `intervals[i][1] + 1 >= val`.

### Sample Input & Output
- **Input**: `add(1)`, `add(3)`, `add(2)`
- **Output**: `[[1, 3]]`

### Explanation
Stream integers `{1, 2, 3}` coalesce into single interval `[1, 3]`.

### Python Implementation
- [`level_9_data_stream_disjoint_intervals.py`](file:///c:/Users/chakr/Downloads/DSA/15-intervals/level_9_data_stream_disjoint_intervals.py)
