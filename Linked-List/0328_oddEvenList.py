"""
328. Odd Even Linked List
Given the head of a singly linked list, group all the nodes with odd indices
together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain.

Result: 32 ms
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Python Algorithm Interview - 32 ms
    def oddEvenList(self, head: ListNode) -> ListNode:
        # Return None if head is None
        if head is None:
            return None

        # Odd points head
        odd = head
        # Even points head.next
        even = head.next
        # Even_head points head.next
        even_head = head.next

        # Loop through linked list
        while even and even.next:
            # Odd and even node moves two steps in each move
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        
        # Link the last node of odd linked list to even_head
        odd.next = even_head

        return head
