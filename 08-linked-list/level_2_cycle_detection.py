"""
Level 2: Linked List Cycle II (Floyd's Algorithm)

Topics Covered:
1. Linked List Cycle II (Find exact node where cycle begins) O(N) time, O(1) space

Mathematical Proof:
Distance traveled by slow = L + K
Distance traveled by fast = L + nC + K = 2(L + K) => L = nC - K
where L is distance from head to cycle entrance, K is distance from entrance to meeting point, C is cycle length.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detect_cycle_start(head: ListNode) -> ListNode:
    """
    Returns the node where the cycle begins. If no cycle exists, returns None.
    """
    if not head or not head.next:
        return None
        
    slow = head
    fast = head
    has_cycle = False
    
    # Phase 1: Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
            
    if not has_cycle:
        return None
        
    # Phase 2: Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
        
    return slow


if __name__ == "__main__":
    # Create Linked List with Cycle: 3 -> 2 -> 0 -> -4 -> (back to 2)
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2  # Cycle back to n2
    
    assert detect_cycle_start(n1) == n2
    
    # Test Linear List (No Cycle)
    n_a = ListNode(1, ListNode(2))
    assert detect_cycle_start(n_a) is None
    
    print("[SUCCESS] All Level 2 Cycle Detection tests passed!")
