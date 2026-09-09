"""
Level 1: Linked List Basics & Pointer Manipulations

Topics Covered:
1. Reverse Linked List (In-Place Iterative) O(N)
2. Middle of Linked List (Fast & Slow Pointers) O(N)

Complexity:
- Time Complexity: O(N) single pass.
- Space Complexity: O(1) in-place auxiliary space.
"""

class ListNode:
    """Definition for singly-linked list node."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(arr: list[int]) -> ListNode:
    """Helper to convert Python list to linked list."""
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def linked_list_to_list(head: ListNode) -> list[int]:
    """Helper to convert linked list back to Python list."""
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


def reverse_linked_list(head: ListNode) -> ListNode:
    """
    Reverses a singly-linked list in-place.
    """
    prev = None
    curr = head
    
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        
    return prev


def find_middle_node(head: ListNode) -> ListNode:
    """
    Finds middle node of linked list using Fast & Slow pointers.
    If there are two middle nodes, returns the second middle node.
    """
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow


if __name__ == "__main__":
    # Test Reverse Linked List
    head1 = create_linked_list([1, 2, 3, 4, 5])
    rev_head = reverse_linked_list(head1)
    assert linked_list_to_list(rev_head) == [5, 4, 3, 2, 1]
    
    # Test Middle Node
    head2 = create_linked_list([1, 2, 3, 4, 5])
    mid2 = find_middle_node(head2)
    assert mid2.val == 3
    
    head3 = create_linked_list([1, 2, 3, 4, 5, 6])
    mid3 = find_middle_node(head3)
    assert mid3.val == 4
    
    print("[SUCCESS] All Level 1 Linked List tests passed!")
