"""
Level 3: Advanced Merging & Priority Queue on Linked Lists

Topics Covered:
1. Merge K Sorted Lists O(N log K) using Min Heap (heapq)

Complexity:
- Time Complexity: O(N log K) where N is total number of nodes and K is number of lists.
- Space Complexity: O(K) for min heap size.
"""

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists: list[ListNode]) -> ListNode:
    """
    Merges k sorted linked lists into one sorted linked list.
    Uses Min Heap storing (node.val, index, node) tuples.
    """
    min_heap = []
    
    # Push head of each list into heap
    for idx, node in enumerate(lists):
        if node:
            # Include idx as tie-breaker for identical node values
            heapq.heappush(min_heap, (node.val, idx, node))
            
    dummy = ListNode(0)
    curr = dummy
    
    while min_heap:
        val, idx, node = heapq.heappop(min_heap)
        curr.next = node
        curr = curr.next
        
        if node.next:
            heapq.heappush(min_heap, (node.next.val, idx, node.next))
            
    return dummy.next


def build_list(vals):
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def to_vals(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


if __name__ == "__main__":
    # Test Merge K Sorted Lists
    l1 = build_list([1, 4, 5])
    l2 = build_list([1, 3, 4])
    l3 = build_list([2, 6])
    
    merged = merge_k_lists([l1, l2, l3])
    assert to_vals(merged) == [1, 1, 2, 3, 4, 4, 5, 6]
    
    print("[SUCCESS] All Level 3 Merge K Lists tests passed!")
