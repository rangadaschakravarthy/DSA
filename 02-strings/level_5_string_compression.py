"""
Level 5: In-Place String Compression & Encoding

Topics Covered:
1. String Compression (Run-Length Encoding In-Place O(N) time, O(1) space)

Complexity:
- Time Complexity: O(N) single pass.
- Space Complexity: O(1) in-place write pointer.
"""

def compress_string(chars: list[str]) -> int:
    """
    Compresses array of characters in-place using run-length encoding.
    Returns the new length of the compressed array.
    """
    write_idx = 0
    read_idx = 0
    
    while read_idx < len(chars):
        char = chars[read_idx]
        count = 0
        
        while read_idx < len(chars) and chars[read_idx] == char:
            read_idx += 1
            count += 1
            
        chars[write_idx] = char
        write_idx += 1
        
        if count > 1:
            for digit in str(count):
                chars[write_idx] = digit
                write_idx += 1
                
    return write_idx


if __name__ == "__main__":
    # Test String Compression
    chars1 = ["a","a","b","b","c","c","c"]
    new_len1 = compress_string(chars1)
    assert new_len1 == 6
    assert chars1[:6] == ["a","2","b","2","c","3"]
    
    chars2 = ["a"]
    assert compress_string(chars2) == 1
    
    print("[SUCCESS] All Level 5 String Compression tests passed!")
