"""
Level 5: Reorganize String

Problem:
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrange of s or return "" if not possible.

Time Complexity: O(N log A) where A is alphabet size
Space Complexity: O(A) heap size
"""
from collections import Counter
import heapq

def reorganize_string(s: str) -> str:
    counts = Counter(s)
    max_heap = [(-freq, char) for char, freq in counts.items()]
    heapq.heapify(max_heap)
    
    prev_freq, prev_char = 0, ""
    res = []
    
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        res.append(char)
        
        if prev_freq < 0:
            heapq.heappush(max_heap, (prev_freq, prev_char))
            
        prev_freq, prev_char = freq + 1, char
        
    result = "".join(res)
    return result if len(result) == len(s) else ""


if __name__ == "__main__":
    assert reorganize_string("aab") == "aba"
    assert reorganize_string("aaab") == ""
    print("[PASS] Level 5 Reorganize String tests passed!")
