"""
Level 6: Add Two Numbers Represented by Linked Lists

Problem:
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

Time Complexity: O(max(N, M))
Space Complexity: O(max(N, M)) for output list
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(arr: list[int]) -> ListNode:
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def linked_list_to_list(head: ListNode) -> list[int]:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    curr = dummy
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        curr.next = ListNode(total % 10)
        curr = curr.next
        
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
            
    return dummy.next


if __name__ == "__main__":
    l1 = create_linked_list([2, 4, 3])  # 342
    l2 = create_linked_list([5, 6, 4])  # 465
    res = add_two_numbers(l1, l2)
    assert linked_list_to_list(res) == [7, 0, 8]  # 807
    
    l3 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l4 = create_linked_list([9, 9, 9, 9])
    res2 = add_two_numbers(l3, l4)
    assert linked_list_to_list(res2) == [8, 9, 9, 9, 0, 0, 0, 1]
    
    print("[PASS] Level 6 Add Two Numbers tests passed!")
