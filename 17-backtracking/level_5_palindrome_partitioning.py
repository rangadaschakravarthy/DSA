"""
Level 5: Palindrome Partitioning

Problem:
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

Time Complexity: O(N * 2^N)
Space Complexity: O(N) recursion stack
"""

def partition(s: str) -> list[list[str]]:
    result = []

    def is_palindrome(sub):
        return sub == sub[::-1]

    def backtrack(start_idx, current_partition):
        if start_idx == len(s):
            result.append(list(current_partition))
            return

        for end_idx in range(start_idx + 1, len(s) + 1):
            sub_str = s[start_idx:end_idx]
            if is_palindrome(sub_str):
                current_partition.append(sub_str)
                backtrack(end_idx, current_partition)
                current_partition.pop()

    backtrack(0, [])
    return result


if __name__ == "__main__":
    res = partition("aab")
    assert ["a", "a", "b"] in res
    assert ["aa", "b"] in res
    assert len(res) == 2
    print("[PASS] Level 5 Palindrome Partitioning tests passed!")
