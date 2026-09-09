"""
Level 8: LRU Cache Implementation

Problem:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement LRUCache class:
- `LRUCache(capacity: int)` Initialize capacity.
- `get(key: int) -> int` Return value of key if exists, else -1.
- `put(key: int, value: int)` Update or insert key-value. Evict least recently used key if capacity exceeded.

Both get and put operations must run in O(1) average time complexity.

Approach: Doubly Linked List + Hashmap
"""

class DNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> DNode
        
        # Dummy head and tail
        self.head = DNode()
        self.tail = DNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: DNode):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node: DNode):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_head(node)
        else:
            if len(self.cache) >= self.cap:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            
            new_node = DNode(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)


if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1
    lru.put(3, 3)  # evicts key 2
    assert lru.get(2) == -1
    lru.put(4, 4)  # evicts key 1
    assert lru.get(1) == -1
    assert lru.get(3) == 3
    assert lru.get(4) == 4
    print("[PASS] Level 8 LRU Cache tests passed!")
