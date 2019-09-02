# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        result = ListNode(0)
        temp = result
        while l1 or l2 or carry:
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)
            s = carry + l1.val + l2.val
            digit = s % 10
            carry = s//10
            result.next = ListNode(digit)
            result = result.next
            l1 = l1.next
            l2 = l2.next
        return temp.next
