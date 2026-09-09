# Topic 14: Greedy Algorithms (Level 1 to Level 9)

A Greedy algorithm builds up a solution piece by piece, making the locally optimal choice at each step with the hope of finding a globally optimal solution.

---

## Level-1: Assign Cookies

### Question
Maximize the number of content children given child greed factors and cookie sizes.

### Description / Explanation
Greedily satisfy children with smallest valid cookie size.

### Logic / Approach
Sort children and cookies array; step cookie index continuously while incrementing child index when cookie $\ge$ greed.

### Sample Input & Output
- **Input**: `g = [1, 2, 3]`, `s = [1, 1]`
- **Output**: `1`

### Explanation
1 child satisfied (greed 1 with cookie size 1).

### Python Implementation
- [`level_1_assign_cookies.py`](file:///c:/Users/chakr/Downloads/DSA/14-greedy/level_1_assign_cookies.py)

---

## Level-2: Jump Game I & II

### Question
1. Jump Game I: Determine if you can reach last index.
2. Jump Game II: Find minimum jumps needed to reach last index.

### Description / Explanation
Track maximum reachable index dynamically.

### Logic / Approach
Update `max_reach = max(max_reach, i + nums[i])`. In Jump Game II, increment jump count when index reaches `curr_end`.

### Sample Input & Output
- **Input**: `[2, 3, 1, 1, 4]`
- **Output**: `can_jump = True`, `min_jumps = 2`

### Explanation
Jump $0 \rightarrow 1 \rightarrow 4$ (2 jumps).

### Python Implementation
- [`level_2_jump_game.py`](file:///c:/Users/chakr/Downloads/DSA/14-greedy/level_2_jump_game.py)

---

## Level-3: Gas Station

### Question
Find starting gas station index to complete circular journey.

### Description / Explanation
If total gas $\ge$ total cost, a valid starting station is guaranteed to exist.

### Logic / Approach
If `current_tank < 0`, reset start index to `i + 1` and reset tank to 0.

### Sample Input & Output
- **Input**: `gas = [1,2,3,4,5]`, `cost = [3,4,5,1,2]`
- **Output**: `3`

### Explanation
Start at index 3 (gas 4, cost 1).

### Python Implementation
- [`level_3_gas_station.py`](file:///c:/Users/chakr/Downloads/DSA/14-greedy/level_3_gas_station.py)

---

## Level-4: Hand of Straights

### Question
Rearrange cards into groups of `groupSize` consisting of consecutive values.

### Description / Explanation
Count frequencies and greedily build consecutive groups starting from smallest available card.

### Logic / Approach
Sort unique keys, decrement frequencies for `groupSize` consecutive numbers.

### Sample Input & Output
- **Input**: `hand = [1,2,3,6,2,3,4,7,8]`, `groupSize = 3`
- **Output**: `True`

### Explanation
Groups: `[1,2,3]`, `[2,3,4]`, `[6,7,8]`.

### Python Implementation
- [`level_4_hand_of_straights.py`](file:///c:/Users/chakr/Downloads/DSA/14-greedy/level_4_hand_of_straights.py)

---

## Level-5: Partition Labels

### Question
Partition string into max number of parts such that every letter appears in at most one part.

### Description / Explanation
Find last occurrence index of every character.

### Logic / Approach
Iterate through string, maintaining maximum `last_occurrence` seen so far. When current index equals max end, finalize partition block.

### Sample Input & Output
- **Input**: `"ababcbacadefegdehijhklij"`
- **Output**: `[9, 7, 8]`

### Explanation
Partitions: `"ababcbaca"`, `"defegde"`, `"hijhklij"`.

### Python Implementation
- [`level_5_partition_labels.py`](file:///c:/Users/chakr/Downloads/DSA/14-greedy/level_5_partition_labels.py)

---

## Level-6: Task Scheduler (Greedy Approach)

### Question
Find minimum time to schedule CPU tasks with cooldown $N$.

### Description / Explanation
Math / Greedy formula based on frequency bottlenecks.

### Logic / Approach
Calculate empty slots created by most frequent task: `len(tasks) + max(0, empty_slots - available_tasks)`.

### Sample Input & Output
- **Input**: `tasks = ["A","A","A","B","B","B"]`, `n = 2`
- **Output**: `8`

### Explanation
Schedule: `A B idle A B idle A B` (8 time units).

### Python Implementation
- [`level_6_greedy_task_scheduler.py`](file:///c:/Users/chakr/Downloads/DSA/14-greedy/level_6_greedy_task_scheduler.py)

---

## Level-7: Candy Distribution

### Question
Distribute candies to children in a line such that higher rating children get more candies than neighbors.

### Description / Explanation
Two-pass greedy strategy (Left-to-Right & Right-to-Left).

### Logic / Approach
1. Pass 1 (Left to Right): If `rating[i] > rating[i-1]`, set `candies[i] = candies[i-1] + 1`.
2. Pass 2 (Right to Left): If `rating[i] > rating[i+1]`, set `candies[i] = max(candies[i], candies[i+1] + 1)`.

### Sample Input & Output
- **Input**: `ratings = [1, 0, 2]`
- **Output**: `5`

### Explanation
Candies assigned: `[2, 1, 2]`. Total $= 5$.

### Python Implementation
- [`level_7_candy_distribution.py`](file:///c:/Users/chakr/Downloads/DSA/14-greedy/level_7_candy_distribution.py)

---

## Level-8: Minimum Number of Refueling Stops

### Question
Find minimum refueling stops to reach target destination starting with `startFuel`.

### Description / Explanation
Greedily store fuel amounts of passed stations in a Max-Heap; pop max fuel when current fuel is exhausted.

### Logic / Approach
Push reachable gas station fuels into Max-Heap. When out of fuel, pop largest fuel station available.

### Sample Input & Output
- **Input**: `target = 100`, `startFuel = 10`, `stations = [[10,60],[20,30],[30,30],[60,40]]`
- **Output**: `2`

### Explanation
Refuel at station 1 (60 fuel) and station 4 (40 fuel) $\rightarrow$ total fuel 110.

### Python Implementation
- [`level_8_min_refueling_stops.py`](file:///c:/Users/chakr/Downloads/DSA/14-greedy/level_8_min_refueling_stops.py)

---

## Level-9: Create Maximum Number

### Question
Create maximum number of length $K$ from digits of two arrays preserving relative order.

### Description / Explanation
Greedy monotonic stack for individual max sub-sequences + greedy merge.

### Logic / Approach
Try all splits $I$ and $K-I$ for lengths picked from `nums1` and `nums2`. Greedily merge both sub-sequences.

### Sample Input & Output
- **Input**: `nums1 = [3,4,6,5]`, `nums2 = [9,1,2,5,8,3]`, `k = 5`
- **Output**: `[9, 8, 6, 5, 3]`

### Explanation
Selected max sub-sequence elements forming largest integer.

### Python Implementation
- [`level_9_create_maximum_number.py`](file:///c:/Users/chakr/Downloads/DSA/14-greedy/level_9_create_maximum_number.py)
