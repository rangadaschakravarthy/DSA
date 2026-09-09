"""
Level 7: Candy Distribution

Problem:
There are n children standing in a line. Each child is assigned a rating value given in ratings array.
- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute.

Time Complexity: O(N)
Space Complexity: O(N)
"""

def candy(ratings: list[int]) -> int:
    n = len(ratings)
    candies = [1] * n
    
    # Left-to-Right pass
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
            
    # Right-to-Left pass
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
            
    return sum(candies)


if __name__ == "__main__":
    assert candy([1, 0, 2]) == 5
    assert candy([1, 2, 2]) == 4
    print("[PASS] Level 7 Candy Distribution tests passed!")
