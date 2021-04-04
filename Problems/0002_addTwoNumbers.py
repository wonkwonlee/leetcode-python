"""
2. Add Two Numbers
Given two non-empty linked lists representing two non-negative integers, 
add the two numbers and return the sum as a linked list

The digits are stored in reverse order, and each of their nodes contains a single digit. 


divmod(a, b) : Returns quotient and remainder as a tuple (q, r)
divmod(10, 3)
>> (3, 1)

간단하게 푸는 방법으로는 ListNode를 전부 List로 바꿔 계산하고 다시 ListNode를 만드는 방법이 있다.
ListNode를 업데이트 하면 기존의 데이터가 덮어 씌워지는게 문제였다.
간단하게 2개의 ListNode를 생성해서 얕은 복사로 같이 Update 시킨다.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # My Attempt - Had to consider if l1 and l2 have different size

    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

    #     root = l3 = ListNode()

    #     carry = 0
    #     while l1 is not None:
    #         val = (l1.val + l2.val) % 10 + carry
    #         carry = (l1.val + l2.val) // 10

    #         l1 = l1.next
    #         l2 = l2.next
    #         l3.next = ListNode(val)
    #         l3 = l3.next 

    #     return root.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Result for final answer and head for temporary calculation
        result = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            # Sum of the two digits
            sum_val = 0

            # Sum of l1 and l2 needs to be added separately; error if different size
            if l1:
                sum_val += l1.val  # l1 value added to sum
                l1 = l1.next  # Update l1 to l1.next
            if l2:
                sum_val += l2.val  # l2 value added to sum
                l2 = l2.next  # Update l1 to l2.next

            # Calculate quotient and remainder
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)  # head.next = current val
            head = head.next  # Update head to head.next

        return result.next
