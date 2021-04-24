"""
Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list 
and return its head.

# Runner method

Result:
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # My Code
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Count the number of nodes
        count = 0
        temp = head
        while temp:
            temp = temp.next
            count += 1

        # Find the nth index from the beginning
        index = count - n

        # If index is 0, skip the first node
        if index == 0:
            if head.next is None:
                return None
            head = head.next
            return head
        
        curr = head
        for i in range(index - 1):
            curr = curr.next
        curr.next = curr.next.next

        return head

    # Example Code - 20 ms
    # Using Runner method
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head

        # Length is the total length of linked list
        length = 0
        while fast:
            # Slow moves only if current length exceeds the target 
            # Current legnth + target = total length
            if length > n:
                slow = slow.next
            # Fast moves every time until it reaches to the end
            fast = fast.next
            length += 1
        
        # If Length and target is different, slow skips the next node
        if slow.next and length != n:
            slow.next = slow.next.next
        
        # If Length and target is same, remove the first node
        if length == n:
            return head.next

        return head
