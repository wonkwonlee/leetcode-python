"""
203. Remove Linked List Elements
Given the head of a linked list and an integer val, remove all the nodes of the 
linked list that has Node.val == val, and return the new head.


# Shallow Copy vs Deep Copy
Initialize a new pointer node to shallow copy the original node.
Move pointer node to track and return the original node.
Any modification in the pointer node affects the original.

Result: 64 ms
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # Remove first node if value is val
        while head is not None and head.val == val:
            head = head.next

        # Return None if head is None
        if head is None:
            return head

        # Shallow copy of head node
        curr = head
        # Loop if curr and next node are both not None and stops if next is None
        while curr is not None and curr.next is not None:
            # If next value is val, continue to the node after next node
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head
