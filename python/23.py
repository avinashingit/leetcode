# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        head = temp = ListNode(0)
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, l))
        while heap:
            val, node = heapq.heappop(heap)
            temp.next = ListNode(val)
            temp = temp.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, node))
        return head.next
