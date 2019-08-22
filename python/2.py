# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        total = ListNode(0)
        copy = total
        while l1 or l2 or carry:
            l1val = 0 if not l1 else l1.val
            l2val = 0 if not l2 else l2.val
            s = l1val + l2val + carry
            digit = s % 10
            carry = s//10
            total.next = ListNode(digit)
            total = total.next
            l1 = None if not l1 else l1.next
            l2 = None if not l2 else l2.next
        return copy.next
