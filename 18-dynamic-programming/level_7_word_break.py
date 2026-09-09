"""
Level 7: Word Break I & II

Problem:
1. Word Break I: Given a string s and a dictionary wordDict, return true if s can be segmented into words.
2. Word Break II: Return all possible sentences where s is segmented into dictionary words.

Time Complexity: O(N^2) for Word Break I
Space Complexity: O(N)
"""

def word_break(s: str, wordDict: list[str]) -> bool:
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[len(s)]


def word_break_ii(s: str, wordDict: list[str]) -> list[str]:
    word_set = set(wordDict)
    memo = {}

    def dfs(idx):
        if idx in memo:
            return memo[idx]
        if idx == len(s):
            return [""]

        res = []
        for end in range(idx + 1, len(s) + 1):
            word = s[idx:end]
            if word in word_set:
                sub_sentences = dfs(end)
                for sub in sub_sentences:
                    res.append((word + " " + sub).strip())

        memo[idx] = res
        return res

    return dfs(0)


if __name__ == "__main__":
    assert word_break("leetcode", ["leet", "code"]) == True
    assert word_break("applepenapple", ["apple", "pen"]) == True
    assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
    
    wb2_res = word_break_ii("catsanddog", ["cat", "cats", "and", "sand", "dog"])
    assert "cat sand dog" in wb2_res
    assert "cats and dog" in wb2_res
    print("[PASS] Level 7 Word Break I & II tests passed!")
