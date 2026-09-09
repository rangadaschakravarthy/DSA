"""
Level 6: Decode String

Problem:
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets 
is being repeated exactly k times. k is guaranteed to be a positive integer.

Time Complexity: O(N) where N is length of decoded string.
Space Complexity: O(N) stack depth.
"""

def decode_string(s: str) -> str:
    def decode(idx):
        res = ""
        k = 0
        while idx < len(s):
            char = s[idx]
            if char.isdigit():
                k = k * 10 + int(char)
            elif char == '[':
                sub_str, idx = decode(idx + 1)
                res += k * sub_str
                k = 0
            elif char == ']':
                return res, idx
            else:
                res += char
            idx += 1
        return res, idx

    result, _ = decode(0)
    return result


if __name__ == "__main__":
    assert decode_string("3[a]2[bc]") == "aaabcbc"
    assert decode_string("3[a2[c]]") == "accaccacc"
    assert decode_string("2[abc]3[cd]ef") == "abcabccdcdcdef"
    print("[PASS] Level 6 Decode String tests passed!")
