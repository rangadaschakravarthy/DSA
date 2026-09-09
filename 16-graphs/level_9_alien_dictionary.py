"""
Level 9: Alien Dictionary (Topological Sort with Edge Cases)

Problem:
There is a new alien language that uses the English alphabet. 
However, the order among the letters is unknown to you.
Given a list of words from the alien language dictionary sorted lexicographically, 
return a string of the unique letters in the new alien language sorted in lexicographically increasing order.
If no valid order exists, return "".

Time Complexity: O(C) total length of words
Space Complexity: O(1) max 26 unique characters
"""
from collections import defaultdict, deque

def alien_order(words: list[str]) -> str:
    adj = {char: set() for word in words for char in word}
    in_degree = {char: 0 for char in adj}
    
    # Build graph
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        
        # Check invalid prefix case (e.g. "abc" before "ab")
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ""
            
        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in adj[w1[j]]:
                    adj[w1[j]].add(w2[j])
                    in_degree[w2[j]] += 1
                break

    # Kahn's BFS Topological Sort
    queue = deque([char for char in in_degree if in_degree[char] == 0])
    result = []
    
    while queue:
        char = queue.popleft()
        result.append(char)
        for neighbor in adj[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                
    return "".join(result) if len(result) == len(adj) else ""


if __name__ == "__main__":
    words1 = ["wrt", "wrf", "er", "ett", "rftt"]
    assert alien_order(words1) == "wertf"
    
    words2 = ["z", "x"]
    assert alien_order(words2) == "zx"
    
    words3 = ["z", "x", "z"]
    assert alien_order(words3) == ""
    print("[PASS] Level 9 Alien Dictionary tests passed!")
