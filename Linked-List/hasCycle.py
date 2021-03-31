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
    def hasCycle(self, head: ListNode) -> bool:
        if  head is None or head.next is None:
            return False

        values = []
        while True:
            # Return false if there is no more node : acyclic
            if head.next is None:
                return False
            else:
                values.append(head.val)
                head = head.next    # Update to next node
                
            for i in range(len(values)):
                # # Current element appears in the list more than once
                # if values.count(values[i]) > 1:
                    for j in range(i + 1, len(values)):
                        if values[i] == values[j] and values[j-1] == values[2*j-i-1]:
                            return True












