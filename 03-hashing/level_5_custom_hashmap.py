"""
Level 5: Custom HashMap Design (Chaining Method)

Topics Covered:
1. Design HashMap without using built-in hash table libraries O(1) average time

Structure:
Uses bucket array of size 1000 and chaining for collision resolution.
"""

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[idx]):
            if k == key:
                self.buckets[idx][i] = (key, value)
                return
        self.buckets[idx].append((key, value))

    def get(self, key: int) -> int:
        idx = self._hash(key)
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[idx]):
            if k == key:
                del self.buckets[idx][i]
                return


if __name__ == "__main__":
    # Test Custom HashMap
    h_map = MyHashMap()
    h_map.put(1, 1)
    h_map.put(2, 2)
    assert h_map.get(1) == 1
    assert h_map.get(3) == -1
    h_map.put(2, 1)  # Update existing key
    assert h_map.get(2) == 1
    h_map.remove(2)
    assert h_map.get(2) == -1
    
    print("[SUCCESS] All Level 5 Custom HashMap tests passed!")
