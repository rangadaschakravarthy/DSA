"""
Level 6: Advanced Frequency Map Window Search

Topics Covered:
1. Minimum Window Substring Frequency Matching O(N)

Complexity:
- Time Complexity: O(N) single pass.
- Space Complexity: O(1) character map space.
"""

from collections import Counter

def min_window(s: str, t: str) -> str:
    """Finds smallest window in s containing all characters of t."""
    if not s or not t:
        return ""
        
    target = Counter(t)
    required = len(target)
    window = {}
    formed = 0
    
    ans = (float('inf'), None, None)
    left = 0
    
    for right, char in enumerate(s):
        window[char] = window.get(char, 0) + 1
        if char in target and window[char] == target[char]:
            formed += 1
            
        while left <= right and formed == required:
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
                
            left_char = s[left]
            window[left_char] -= 1
            if left_char in target and window[left_char] < target[left_char]:
                formed -= 1
            left += 1
            
    return "" if ans[0] == float('inf') else s[ans[1] : ans[2] + 1]


if __name__ == "__main__":
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    
    print("[SUCCESS] All Level 6 Frequency Window Hash tests passed!")
