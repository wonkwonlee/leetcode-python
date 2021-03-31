"""
Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it.
Return True if there is a cycle in the linked list. Otherwise, return False.

A cycle in a linked list is defined if there is some node in the list that can be 
reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer 
is connected to. 
Note that pos is not passed as a parameter.



Result:
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isCycle(val):
        set_val = list(set(val))
        if len(set_val) == len(val):
            return True
        else:
            return False


    def hasCycle(self, head: ListNode) -> bool:
        
        if head.next is None:
            return False

        curr = head
        curr_val = []
        while True:
            curr_val.append(curr.val)
            if curr.next is None:
                return False
            else:
                curr = head.next

