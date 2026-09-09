"""
Level 5: Partition Labels

Problem:
You are given a string s. We want to partition the string into as many parts as possible 
so that each letter appears in at most one part. Return a list of integers representing size of parts.

Time Complexity: O(N)
Space Complexity: O(1) fixed size 26 map
"""

def partition_labels(s: str) -> list[int]:
    last_occurrence = {char: i for i, char in enumerate(s)}
    
    result = []
    start = 0
    end = 0
    
    for i, char in enumerate(s):
        end = max(end, last_occurrence[char])
        if i == end:
            result.append(end - start + 1)
            start = i + 1
            
    return result


if __name__ == "__main__":
    assert partition_labels("ababcbacadefegdehijhklij") == [9, 7, 8]
    assert partition_labels("eccbbbbdec") == [10]
    print("[PASS] Level 5 Partition Labels tests passed!")
