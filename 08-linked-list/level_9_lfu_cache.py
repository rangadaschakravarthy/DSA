"""
Level 9: LFU (Least Frequently Used) Cache Implementation

Problem:
Design and implement a data structure for a Least Frequently Used (LFU) cache.
- `LFUCache(capacity: int)` Initialize capacity.
- `get(key: int) -> int` Return value of key if exists, else -1. Increments frequency count.
- `put(key: int, value: int)` Update or insert value. When capacity reached, evict least frequently used key. 
  If tie in frequency, evict least recently used key among them.

Time Complexity: O(1) average for both get and put.
Space Complexity: O(N) where N is capacity.
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

    def add_to_head(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove_node(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_tail(self) -> Node:
        if self.size == 0:
            return None
        tail_node = self.tail.prev
        self.remove_node(tail_node)
        return tail_node


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_map = {}  # key -> Node
        self.freq_map = defaultdict(DoublyLinkedList)  # freq -> DoublyLinkedList
        self.min_freq = 0

    def _update_freq(self, node: Node):
        freq = node.freq
        self.freq_map[freq].remove_node(node)
        
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
                min_dll = self.freq_map[self.min_freq]
                evict_node = min_dll.tail.prev
                min_dll.remove_node(evict_node)
                del self.key_map[evict_node.key]

            new_node = Node(key, value)
            self.key_map[key] = new_node
            self.freq_map[1].add_to_head(new_node)
            self.min_freq = 1


if __name__ == "__main__":
    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(2, 2)
    assert lfu.get(1) == 1       # returns 1, freq(1)=2, freq(2)=1
    lfu.put(3, 3)                # evicts key 2 (freq 1)
    assert lfu.get(2) == -1      # returns -1 (not found)
    assert lfu.get(3) == 3       # returns 3, freq(3)=2
    lfu.put(4, 4)                # evicts key 1 (freq 2, LRU tie breaker)
    assert lfu.get(1) == -1      # returns -1
    assert lfu.get(3) == 3       # returns 3
    assert lfu.get(4) == 4       # returns 4
    print("[PASS] Level 9 LFU Cache tests passed!")
