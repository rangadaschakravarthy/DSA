"""
Level 5: Grouped Pointer Reversal (Reverse Nodes in K-Group)

Topics Covered:
1. Reverse Nodes in K-Group O(N) time, O(1) space

Algorithm:
1. Check if there are at least k nodes remaining. If not, leave them unchanged.
2. Reverse k nodes in-place.
3. Recursively call reverse_k_group for the remainder and attach!
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_kth_node(curr: ListNode, k: int) -> ListNode:
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr


def reverse_k_group(head: ListNode, k: int) -> ListNode:
    """
    Reverses nodes of a linked list k at a time and returns its modified list.
    """
    dummy = ListNode(0, head)
    group_prev = dummy
    
    while True:
        kth = get_kth_node(group_prev, k)
        if not kth:
            break
        group_next = kth.next
        
        # Reverse k nodes
        prev, curr = kth.next, group_prev.next
        while curr != group_next:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            
        tmp = group_prev.next
        group_prev.next = kth
        group_prev = tmp
        
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
    l1 = build_list([1, 2, 3, 4, 5])
    r1 = reverse_k_group(l1, 2)
    assert to_vals(r1) == [2, 1, 4, 3, 5]
    
    l2 = build_list([1, 2, 3, 4, 5])
    r2 = reverse_k_group(l2, 3)
    assert to_vals(r2) == [3, 2, 1, 4, 5]
    
    print("[SUCCESS] All Level 5 Reverse K-Group tests passed!")
