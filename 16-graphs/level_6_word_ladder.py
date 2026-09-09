"""
Level 6: Word Ladder (Shortest Transformation Sequence BFS)

Problem:
A transformation sequence from beginWord to endWord using a dictionary wordList is a sequence of words 
where every adjacent pair differs by single letter. Find the length of shortest transformation sequence.

Time Complexity: O(M^2 * N) where M is length of words, N is number of words
Space Complexity: O(M * N)
"""
from collections import deque, defaultdict

def ladder_length(beginWord: str, endWord: str, wordList: list[str]) -> int:
    if endWord not in wordList:
        return 0
        
    word_len = len(beginWord)
    all_combo_dict = defaultdict(list)
    
    for word in wordList:
        for i in range(word_len):
            pattern = word[:i] + "*" + word[i+1:]
            all_combo_dict[pattern].append(word)
            
    queue = deque([(beginWord, 1)])
    visited = set([beginWord])
    
    while queue:
        current_word, level = queue.popleft()
        for i in range(word_len):
            pattern = current_word[:i] + "*" + current_word[i+1:]
            for neighbor in all_combo_dict[pattern]:
                if neighbor == endWord:
                    return level + 1
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))
            all_combo_dict[pattern] = []  # Clear pattern to prevent duplicate traversals
            
    return 0


if __name__ == "__main__":
    wlist = ["hot", "dot", "dog", "lot", "log", "cog"]
    assert ladder_length("hit", "cog", wlist) == 5
    assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    print("[PASS] Level 6 Word Ladder tests passed!")
