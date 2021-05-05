"""
Palindrome Linked List
Given the head of a singly linked list, return true if it is a palindrome.

# Example
head = [1,2,2,1]
>> True

head = [1,2]
>> False

Result: 
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Copy into Array list - 780 ms
    def isPalindrome(self, head: ListNode) -> bool:

        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        return arr == arr[::-1]

    # Using linked list, O(n) time and O(1) space
    def isPalindrome(self, head: ListNode) -> bool:

        if head is None:
            return None

        prev, curr, temp = None, head


        return True







