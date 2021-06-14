"""
21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two lists.


# Example
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: l1 = [], l2 = []
Output: []

Input: l1 = [], l2 = [0]
Output: [0]

Result: 24 ms
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Boundary cases
        if l1 is None and l2 is None:
            return None
        elif l1 is None and l2:
            return l2
        elif l2 is None and l1:
            return l1

        # Initialize a new linked list node
        node = ListNode(0)
        
        # Current pointer
        curr = node
        while l1 and l2:
            # Compare current l1 and l2 value
            if l1.val <= l2.val:
                curr.next = ListNode(l1.val)
                l1 = l1.next
            else:
                curr.next = ListNode(l2.val)
                l2 = l2.next
            curr = curr.next
        
        # Add rest of linked list
        if l1 is None:
            curr.next = l2
        if l2 is None:
            curr.next = l1

        return node.next
