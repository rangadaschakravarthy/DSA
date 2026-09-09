"""
Level 7: Flatten a Multilevel Doubly Linked List

Problem:
You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, 
and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, 
also containing these special nodes. Flatten the list so that all the nodes appear in a single-level, 
doubly linked list.

Time Complexity: O(N)
Space Complexity: O(N) call stack / explicit stack
"""

class Node:
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def flatten(head: Node) -> Node:
    if not head:
        return None
        
    curr = head
    while curr:
        if curr.child:
            nxt = curr.next
            child_head = flatten(curr.child)
            
            curr.next = child_head
            child_head.prev = curr
            curr.child = None
            
            # Move to the end of the flattened child list
            tail = child_head
            while tail.next:
                tail = tail.next
                
            tail.next = nxt
            if nxt:
                nxt.prev = tail
                
        curr = curr.next
        
    return head


def to_list(head: Node) -> list[int]:
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res


if __name__ == "__main__":
    # Create nodes 1-2-3 with 3 having child 4-5
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    
    n1.next = n2; n2.prev = n1
    n2.next = n3; n3.prev = n2
    
    n3.child = n4
    n4.next = n5; n5.prev = n4
    
    flattened = flatten(n1)
    assert to_list(flattened) == [1, 2, 3, 4, 5]
    
    print("[PASS] Level 7 Flatten Multilevel Doubly Linked List tests passed!")
