"""
Level 9: IPO (Max Profit with K Projects)

Problem:
Suppose LeetCode will start its IPO soon. To maximize your capital after finishing at most k distinct projects:
You are given n projects where the ith project has a pure profit profits[i] and a minimum capital capital[i] needed to start it.
Initially, you have w capital. When you finish a project, you will get its profit added to your total capital.
Return the final maximized capital.

Time Complexity: O(N log N + K log N)
Space Complexity: O(N) max-heap + min-heap storage
"""
import heapq

def find_maximized_capital(k: int, w: int, profits: list[int], capital: list[int]) -> int:
    # Pair projects as (capital, profit) and sort by capital
    projects = sorted(zip(capital, profits))
    n = len(projects)
    max_profit_heap = []
    i = 0

    for _ in range(k):
        # Push all affordable projects into max-profit heap
        while i < n and projects[i][0] <= w:
            heapq.heappush(max_profit_heap, -projects[i][1])
            i += 1

        if not max_profit_heap:
            break

        # Pick the most profitable affordable project
        w += -heapq.heappop(max_profit_heap)

    return w


if __name__ == "__main__":
    assert find_maximized_capital(2, 0, [1, 2, 3], [0, 1, 1]) == 4
    assert find_maximized_capital(3, 0, [1, 2, 3], [0, 1, 2]) == 6
    print("[PASS] Level 9 IPO Max Profit tests passed!")
