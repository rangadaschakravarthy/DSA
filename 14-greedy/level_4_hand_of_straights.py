"""
Level 4: Hand of Straights

Problem:
Alice has a hand of cards, given as an array of integers. 
Rearrange cards into groups so that each group has size groupSize, and consists of groupSize consecutive cards.

Time Complexity: O(N log N)
Space Complexity: O(N)
"""
from collections import Counter

def is_n_straight_hand(hand: list[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0:
        return False
        
    counts = Counter(hand)
    sorted_keys = sorted(counts.keys())
    
    for card in sorted_keys:
        if counts[card] > 0:
            count = counts[card]
            for i in range(groupSize):
                if counts[card + i] < count:
                    return False
                counts[card + i] -= count
                
    return True


if __name__ == "__main__":
    assert is_n_straight_hand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) == True
    assert is_n_straight_hand([1, 2, 3, 4, 5], 4) == False
    print("[PASS] Level 4 Hand of Straights tests passed!")
