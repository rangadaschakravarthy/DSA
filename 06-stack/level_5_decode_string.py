"""
Level 5: Nested Character Decoding Stack

Topics Covered:
1. Decode String 3[a2[c]] -> "accaccacc" O(N) time, O(N) space

Logic:
Maintain stack storing tuples of (previous_str, repeat_count).
When encountering '[', push current state and reset. When ']', pop state and expand!
"""

def decode_string(s: str) -> str:
    """
    Decodes an encoded string formatted like k[encoded_string].
    """
    stack = []
    curr_str = ""
    curr_num = 0
    
    for char in s:
        if char.isdigit():
            curr_num = curr_num * 10 + int(char)
        elif char == '[':
            stack.append((curr_str, curr_num))
            curr_str = ""
            curr_num = 0
        elif char == ']':
            prev_str, num = stack.pop()
            curr_str = prev_str + curr_str * num
        else:
            curr_str += char
            
    return curr_str


if __name__ == "__main__":
    assert decode_string("3[a]2[bc]") == "aaabcbc"
    assert decode_string("3[a2[c]]") == "accaccacc"
    assert decode_string("2[abc]3[cd]ef") == "abcabccdcdcdef"
    
    print("[SUCCESS] All Level 5 Decode String tests passed!")
