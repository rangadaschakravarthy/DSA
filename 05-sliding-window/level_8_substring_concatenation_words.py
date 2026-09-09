"""
Level 8: Multi-Word Sliding Window & Concatenation Search

Topics Covered:
1. Substring with Concatenation of All Words O(N * word_len)

Complexity:
- Time Complexity: O(N * word_len) where N = len(s).
- Space Complexity: O(K * word_len) for word frequency map.
"""

from collections import Counter

def find_substring(s: str, words: list[str]) -> list[int]:
    """
    Finds all starting indices of substring(s) in s that is a concatenation of each word in words exactly once.
    """
    if not s or not words:
        return []
        
    word_len = len(words[0])
    num_words = len(words)
    total_len = word_len * num_words
    word_counts = Counter(words)
    results = []
    
    for i in range(word_len):
        left = i
        right = i
        current_counts = Counter()
        count = 0
        
        while right + word_len <= len(s):
            w = s[right : right + word_len]
            right += word_len
            
            if w in word_counts:
                current_counts[w] += 1
                count += 1
                
                while current_counts[w] > word_counts[w]:
                    left_word = s[left : left + word_len]
                    current_counts[left_word] -= 1
                    count -= 1
                    left += word_len
                    
                if count == num_words:
                    results.append(left)
            else:
                current_counts.clear()
                count = 0
                left = right
                
    return sorted(results)


if __name__ == "__main__":
    assert find_substring("barfoothefoobarman", ["foo", "bar"]) == [0, 9]
    assert find_substring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]) == []
    
    print("[SUCCESS] All Level 8 Substring Concatenation tests passed!")
