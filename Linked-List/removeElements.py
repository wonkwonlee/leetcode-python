"""
Remove Linked List Elements
Given the head of a linked list and an integer val, remove all the nodes of the 
linked list that has Node.val == val, and return the new head.


# Shallow Copy vs Deep Copy


Result:
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        curr = head
        while curr:
            if curr.val == val:
                break
            prev = curr
            curr = curr.next  

        prev.next = curr.next
        curr = None
        
        return 
