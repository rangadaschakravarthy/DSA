"""
Level 4: Two-Pointer Split & Interleaving Reorder

Topics Covered:
1. Reorder List L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 ... O(N) time, O(1) space

Steps:
1. Find middle of linked list using Fast & Slow pointers.
2. Reverse second half of linked list.
3. Merge/Interleave first half and reversed second half.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head: ListNode) -> None:
    """Reorders linked list in-place."""
    if not head or not head.next:
        return
        
    # Step 1: Find middle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    # Step 2: Reverse second half
    prev, curr = None, slow.next
    slow.next = None  # Cut first half
    
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    second = prev
    first = head
    
    # Step 3: Interleave first and second half
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2


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
    l1 = build_list([1, 2, 3, 4])
    reorder_list(l1)
    assert to_vals(l1) == [1, 4, 2, 3]
    
    l2 = build_list([1, 2, 3, 4, 5])
    reorder_list(l2)
    assert to_vals(l2) == [1, 5, 2, 4, 3]
    
    print("[SUCCESS] All Level 4 Reorder List tests passed!")
