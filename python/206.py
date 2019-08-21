# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cptr, ptr = None, head
        while ptr is not None:
            nptr = ptr.next
            ptr.next = cptr
            cptr = ptr
            ptr = nptr
        return cptr
