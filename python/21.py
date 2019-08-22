# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newList = ListNode(0)
        copy = newList
        while l1 and l2:
            if l1.val < l2.val:
                newList.next = ListNode(l1.val)
                l1 = l1.next
            else:
                newList.next = ListNode(l2.val)
                l2 = l2.next
            newList = newList.next
        newList.next = l1 if l1 else l2
        return copy.next
