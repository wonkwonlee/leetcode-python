"""
Intersection of Two Linked Lists
Given the heads of two singly linked-lists headA and headB, 
return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.

Result: 152 ms
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # Initialize dictionaries
        d1, d2 = {}, {}
        # Initialize value index to 0
        index = 0
        # Store headA linked list to dictionary 1
        while headA:
            # Use linked list as a key and index as a value
            d1[headA] = index
            headA = headA.next
            index += 1

        # Reset value index to 0
        index = 0
        # Store headB linked list to dictionary 2
        while headB:
            d2[headB] = index
            headB = headB.next
            index += 1

        # Initialize headB dictionary keys
        d2_keys = list(d2.keys())
        # From i in range 0 to headB size
        for i in range(index):
            # Check if current d2 key exists in d1
            if d1.get(d2_keys[i]) is not None:
                # Return current d2 key (linked list) 
                return d2_keys[i]

        # If no d2 key exists, return None
        return None
