"""
Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it.
Return True if there is a cycle in the linked list. Otherwise, return False.

A cycle in a linked list is defined if there is some node in the list that can be 
reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer 
is connected to. 
Note that pos is not passed as a parameter.


Set data structure can store not only int or string but also node.

Result: 56 ms
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Method to find a loop in the linked list
def is_cycle(node):
    # Store each node to set
    s = set()
    while node:
        # If current node is visited before, return true
        if node is s:
            return True
        # If current node is first visited, add to set
        s.add(node)
        node = node.next

    return False


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False

        if is_cycle(head):
            return True
        else:
            return False

    # LeetCode example code, 48 ms
    # This code changes node's value to mark visited nodes
    def hasCycle(self, head: ListNode) -> bool:
        while head:
            # Max val is 100000
            if head.val > 100000:
                return True
            # Update the value of visited node to 100001
            head.val = 100001
            head = head.next
        return False
