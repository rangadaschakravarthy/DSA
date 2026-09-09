# 02-Strings Module Curriculum & Problem Guide

---

## Level-1: String Basics & Two-Pointer Verification

### Problem 1: Valid Palindrome (Alphanumeric Clean)
- **Question**: Check if a string `s` is a palindrome, considering only alphanumeric characters and ignoring case.
- **Description / Explanation**: Clean string of non-alphanumeric symbols and compare characters from both ends inwards.
- **Approach & Logic**:
  - Two Pointers: `left = 0`, `right = len(s) - 1`.
  - Skip non-alphanumeric characters using `.isalnum()`.
  - Compare `s[left].lower() == s[right].lower()`.
- **Sample Input**: `s = "A man, a plan, a canal: Panama"`
- **Sample Output**: `True`
- **Explanation**: Cleaned string: `"amanaplanacanalpanama"` is identical read forwards and backwards.
- **Python Implementation**: [`level_1_string_basics.py`](file:///c:/Users/chakr/Downloads/DSA/02-strings/level_1_string_basics.py)

---

## Level-2: Anagram Patterns & Frequency Mapping

### Problem 1: Group Anagrams
- **Question**: Given an array of strings `strs`, group the anagrams together.
- **Description / Explanation**: Group words that have the exact same character frequencies regardless of character order.
- **Approach & Logic**:
  - Create character count tuple of length 26: `tuple(count)` as hash map key.
  - Append original word to dictionary value list: `hashmap[key].append(word)`.
- **Sample Input**: `strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`
- **Sample Output**: `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`
- **Explanation**: `"eat"`, `"tea"`, and `"ate"` all have 1 'a', 1 'e', and 1 't'.
- **Python Implementation**: [`level_2_anagrams.py`](file:///c:/Users/chakr/Downloads/DSA/02-strings/level_2_anagrams.py)

---

## Level-3: Palindromic Substrings & Expand Around Center

### Problem 1: Longest Palindromic Substring
- **Question**: Given a string `s`, return the longest palindromic substring in `s`.
- **Description / Explanation**: Find contiguous palindrome substring of maximum length.
- **Approach & Logic**:
  - Expand Around Center: Test $2N - 1$ centers (N odd centers + N-1 even centers).
  - Expand `left` and `right` outward as long as `s[left] == s[right]`.
- **Sample Input**: `s = "babad"`
- **Sample Output**: `"bab"` (or `"aba"`)
- **Explanation**: Substrings `"bab"` and `"aba"` both have length 3.
- **Python Implementation**: [`level_3_palindromes.py`](file:///c:/Users/chakr/Downloads/DSA/02-strings/level_3_palindromes.py)

---

## Level-4: Sliding Window Substring Algorithms

### Problem 1: Longest Substring Without Repeating Characters
- **Question**: Find the length of the longest substring in `s` without repeating characters.
- **Description / Explanation**: Maintain a variable sliding window of distinct characters in $O(N)$ time.
- **Approach & Logic**:
  - Maintain hash map `char_index_map[char] = index`.
  - When duplicate `char` seen at index $\ge \text{left}$, jump `left = char_index_map[char] + 1`.
- **Sample Input**: `s = "abcabcbb"`
- **Sample Output**: `3`
- **Explanation**: Longest substring without repeating characters is `"abc"` (length 3).
- **Python Implementation**: [`level_4_window_substring.py`](file:///c:/Users/chakr/Downloads/DSA/02-strings/level_4_window_substring.py)

---

## Level-5: In-Place String Compression

### Problem 1: String Compression (Run-Length Encoding)
- **Question**: Compress array of characters in-place using run-length encoding. Return new length.
- **Description / Explanation**: Replace repeated consecutive characters with the character followed by count digits.
- **Approach & Logic**:
  - Pointers: `read_idx` and `write_idx`. Count consecutive identical characters.
  - Write character, then write count digits if count $> 1$.
- **Sample Input**: `chars = ["a", "a", "b", "b", "c", "c", "c"]`
- **Sample Output**: `6` (Array modified to `["a", "2", "b", "2", "c", "3"]`)
- **Explanation**: 2 'a's, 2 'b's, 3 'c's compressed in-place.
- **Python Implementation**: [`level_5_string_compression.py`](file:///c:/Users/chakr/Downloads/DSA/02-strings/level_5_string_compression.py)

---

## Level-6: Knuth-Morris-Pratt (KMP) Pattern Matching

### Problem 1: KMP Pattern Search
- **Question**: Find all 0-indexed starting occurrences of pattern in text in $O(N + M)$ time.
- **Description / Explanation**: Avoid re-checking matching characters upon mismatch using precomputed LPS array.
- **Approach & Logic**:
  1. Build LPS (Longest Prefix Suffix) array for pattern.
  2. Scan text: on mismatch, set `j = lps[j - 1]` instead of resetting to start of pattern.
- **Sample Input**: `text = "ABABDABACDABABCABAB", pattern = "ABABCABAB"`
- **Sample Output**: `[10]`
- **Explanation**: Pattern matches text starting at index 10.
- **Python Implementation**: [`level_6_kmp_matching.py`](file:///c:/Users/chakr/Downloads/DSA/02-strings/level_6_kmp_matching.py)

---

## Level-7: Rabin-Karp Rolling Hash

### Problem 1: Rabin-Karp String Search
- **Question**: Find starting indices of pattern in text using polynomial rolling hash.
- **Description / Explanation**: Match hash values of sliding windows in $O(1)$ amortized time per window shift.
- **Approach & Logic**:
  - Compute initial hash `hash(pattern)` and `hash(text[0..m-1])`.
  - Shift window: `t_hash = (d * (t_hash - text[i]*h) + text[i+m]) % q`.
- **Sample Input**: `text = "GEEKS FOR GEEKS", pattern = "GEEK"`
- **Sample Output**: `[0, 10]`
- **Explanation**: `"GEEK"` matches at index 0 and index 10.
- **Python Implementation**: [`level_7_rabin_karp.py`](file:///c:/Users/chakr/Downloads/DSA/02-strings/level_7_rabin_karp.py)

---

## Level-8: Linear-Time Z-Algorithm

### Problem 1: Z-Algorithm Search
- **Question**: Construct Z-array and locate pattern matches in text in linear $O(N + M)$ time.
- **Description / Explanation**: `Z[i]` stores length of longest substring starting at `i` matching prefix of string.
- **Approach & Logic**:
  - Concatenate `concat = pattern + "$" + text`.
  - Compute Z-array using sliding window $[l, r]$. Find indices where `Z[i] == len(pattern)`.
- **Sample Input**: `text = "baabaa", pattern = "aab"`
- **Sample Output**: `[1]`
- **Explanation**: `"aab"` starts at index 1 in `"baabaa"`.
- **Python Implementation**: [`level_8_z_algorithm.py`](file:///c:/Users/chakr/Downloads/DSA/02-strings/level_8_z_algorithm.py)

---

## Level-9: Suffix Array Mastery

### Problem 1: Longest Common Substring
- **Question**: Find the longest common substring between two strings `s1` and `s2` in $O(N \log N)$ time.
- **Description / Explanation**: Construct Suffix Array for `s1 + "#" + s2 + "$"` and find max LCP between adjacent suffixes from different strings.
- **Approach & Logic**:
  - Build Suffix Array (sorted suffix indices).
  - Compute Longest Common Prefix (LCP) between adjacent suffixes belonging to `s1` and `s2`.
- **Sample Input**: `s1 = "ABABC", s2 = "BABCA"`
- **Sample Output**: `"BABC"`
- **Explanation**: Longest common contiguous substring is `"BABC"` (length 4).
- **Python Implementation**: [`level_9_suffix_array.py`](file:///c:/Users/chakr/Downloads/DSA/02-strings/level_9_suffix_array.py)
