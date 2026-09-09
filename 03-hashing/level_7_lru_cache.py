"""
Level 7: Expert Data Structure Design — LRU Cache

Topics Covered:
1. Design LRU Cache (Doubly Linked List + Hash Map O(1) get & put)

Complexity:
- Time Complexity: O(1) per operation.
- Space Complexity: O(Capacity).
"""

class Node:
    """Doubly Linked List Node."""
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    """Least Recently Used (LRU) Cache."""
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        # Dummy head and tail nodes
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """Removes node from doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node: Node) -> None:
        """Adds node right after dummy head."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_head(node)
        else:
            if len(self.cache) >= self.capacity:
                # Evict least recently used (node right before tail)
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
                
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)


if __name__ == "__main__":
    # Test LRU Cache
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1
    lru.put(3, 3)  # Evicts key 2
    assert lru.get(2) == -1
    lru.put(4, 4)  # Evicts key 1
    assert lru.get(1) == -1
    assert lru.get(3) == 3
    assert lru.get(4) == 4
    
    print("[SUCCESS] All Level 7 LRU Cache tests passed!")
