"""
Level 1: Assign Cookies

Problem:
Assume you are an awesome parent and want to give your children some cookies. 
Each child i has a greed factor g[i], and each cookie j has a size s[j]. 
If s[j] >= g[i], we can assign the cookie j to the child i. 
Maximize the number of your content children.

Time Complexity: O(N log N + M log M)
Space Complexity: O(1)
"""

def find_content_children(g: list[int], s: list[int]) -> int:
    g.sort()
    s.sort()
    
    child_i = 0
    cookie_j = 0
    
    while child_i < len(g) and cookie_j < len(s):
        if s[cookie_j] >= g[child_i]:
            child_i += 1
        cookie_j += 1
        
    return child_i


if __name__ == "__main__":
    assert find_content_children([1, 2, 3], [1, 1]) == 1
    assert find_content_children([1, 2], [1, 2, 3]) == 2
    print("[PASS] Level 1 Assign Cookies tests passed!")
