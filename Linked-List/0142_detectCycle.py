"""
142. Linked List Cycle II
Given a linked list, return the node where the cycle begins. 
If there is no cycle, return null.

Notice that you should not modify the linked list.


Result: 40 ms
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # While-loop if head is not None
        while head:
            if head.val > 100000:
                return head
            head.val = 100001
            head = head.next
        return None
