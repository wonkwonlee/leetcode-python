"""
Reverse Linked List
Given the head of a singly linked list, reverse the list, and 
return the reversed list.

# Example
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []

Result: 24 ms (Recursive) , 32 ms (Iterative)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Recursive method
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node, prev=None):
            """
            # Recursive explanation
            reverse(1, prev=None)
            next = node.next = 2, node.next = prev = None, node = 1
            return reverse(2, 1)

            reverse(2, 1)
            next = node.next = 3, node.next = prev = 1, node = 2
            return reverse(3, 2)
                ~~~
            reverse(5, 4)
            next = node.next = None, node.next = prev = 4, node = 5
            return reverse(None, 5)

            reverse(None, 5)
            return prev = 5

            Thus, 5->4->3->2->1
            """
            if node is None:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)


# Iterative method
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        head = 1
        next = head.next = 2, head.next = prev = None
        prev = head = 1, head = next = 2

        head = 2
        next = head.next = 3, head.next = prev = 1
        prev = head = 2, head = next = 3
            ~~~
        head = 5
        next = head.next = None, head.next = prev = 4
        prev = head = 5, head = next = None

        head = None
        return prev = 5

        Thus, 5->4->3->2->1
        """
        # ListNode prev store reversed linked list
        prev = None
        while head:
            # Update new variable next to head.next, and head.next to prev
            next, head.next = head.next, prev
            # Update prev to current head, and head to next(= head.next)
            prev, head = head, next

        return prev
