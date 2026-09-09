"""
Level 9: Consistent Hashing Ring Design (Mastery Level)

Topics Covered:
1. Consistent Hashing Ring with Virtual Nodes (Distributed Hash Tables)

Concept:
Maps both physical servers and keys to a 32-bit integer ring.
Virtual nodes ensure uniform hash distribution across physical nodes.
"""

import hashlib
import bisect

class ConsistentHashRing:
    def __init__(self, num_replicas: int = 3):
        self.num_replicas = num_replicas
        self.ring = []  # Sorted list of hash values
        self.node_map = {}  # hash value -> physical node name

    def _hash(self, key: str) -> int:
        """MD5 Hash function returning 32-bit integer."""
        return int(hashlib.md5(key.encode('utf-8')).hexdigest()[:8], 16)

    def add_node(self, node: str) -> None:
        """Adds a physical node to the ring with virtual replicas."""
        for i in range(self.num_replicas):
            vnode_key = f"{node}-vnode-{i}"
            h = self._hash(vnode_key)
            bisect.insort(self.ring, h)
            self.node_map[h] = node

    def remove_node(self, node: str) -> None:
        """Removes a physical node from the ring."""
        for i in range(self.num_replicas):
            vnode_key = f"{node}-vnode-{i}"
            h = self._hash(vnode_key)
            idx = bisect.bisect_left(self.ring, h)
            if idx < len(self.ring) and self.ring[idx] == h:
                del self.ring[idx]
                del self.node_map[h]

    def get_node(self, key: str) -> str:
        """Gets nearest physical node clockwise for given key."""
        if not self.ring:
            return None
        h = self._hash(key)
        idx = bisect.bisect_right(self.ring, h)
        if idx == len(self.ring):
            idx = 0  # Wrap around ring to 0
        return self.node_map[self.ring[idx]]


if __name__ == "__main__":
    # Test Consistent Hashing Ring
    ch = ConsistentHashRing(num_replicas=5)
    ch.add_node("Server-A")
    ch.add_node("Server-B")
    ch.add_node("Server-C")
    
    server_1 = ch.get_node("user_1001")
    server_2 = ch.get_node("user_1002")
    assert server_1 in ["Server-A", "Server-B", "Server-C"]
    assert server_2 in ["Server-A", "Server-B", "Server-C"]
    
    print("[SUCCESS] All Level 9 Consistent Hashing Ring Mastery tests passed!")
