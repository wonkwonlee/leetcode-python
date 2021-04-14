"""
Odd Even Linked List
Given the head of a singly linked list, group all the nodes with odd indices
together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain.

Result:
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        count = 1
        array = []
        odd = head
        even = head.next
        while odd:
            if odd.next is None or even.next is None:
                break
        
            print(f"curr:{0}", odd.val)
            if count % 2 == 1:
                print(f"odd:{0}", odd.val)
                odd.next = odd.next.next
                odd = odd.next
            else:
                array.append(even)
                even.next = even.next.next
                even = even.next
            count += 1

        return head
