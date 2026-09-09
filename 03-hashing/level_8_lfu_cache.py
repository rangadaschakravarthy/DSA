"""
Level 8: Interview / CP Advanced Cache Design — LFU Cache

Topics Covered:
1. Design LFU (Least Frequently Used) Cache O(1) time per operation

Complexity:
- Time Complexity: O(1) for get and put.
- Space Complexity: O(Capacity).
"""

from collections import defaultdict

class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_to_head(self, node: Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_tail(self) -> Node:
        if self.size == 0:
            return None
        node = self.tail.prev
        self.remove(node)
        return node


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_map = {}  # key -> Node
        self.freq_map = defaultdict(DoublyLinkedList)  # freq -> DoublyLinkedList
        self.min_freq = 0

    def _update_freq(self, node: Node) -> None:
        freq = node.freq
        self.freq_map[freq].remove(node)
        
        if self.freq_map[freq].size == 0 and self.min_freq == freq:
            self.min_freq += 1
            
        node.freq += 1
        self.freq_map[node.freq].add_to_head(node)

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        node = self.key_map[key]
        self._update_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
            
        if key in self.key_map:
            node = self.key_map[key]
            node.val = value
            self._update_freq(node)
        else:
            if len(self.key_map) >= self.capacity:
                lfu_list = self.freq_map[self.min_freq]
                evicted = lfu_list.remove_tail()
                if evicted:
                    del self.key_map[evicted.key]
                    
            new_node = Node(key, value)
            self.key_map[key] = new_node
            self.freq_map[1].add_to_head(new_node)
            self.min_freq = 1


if __name__ == "__main__":
    # Test LFU Cache
    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(2, 2)
    assert lfu.get(1) == 1       # freq(1)=2, freq(2)=1
    lfu.put(3, 3)                # Evicts key 2 (freq 1)
    assert lfu.get(2) == -1
    assert lfu.get(3) == 3       # freq(3)=2
    lfu.put(4, 4)                # Evicts key 1 (freq 2, tie-breaker LRU)
    assert lfu.get(1) == -1
    assert lfu.get(3) == 3
    assert lfu.get(4) == 4
    
    print("[SUCCESS] All Level 8 LFU Cache tests passed!")
