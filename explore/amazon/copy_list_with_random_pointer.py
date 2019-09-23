"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        result = temp = Node(0, None, None)
        head2 = head
        seen = {}
        while head:
            result.next = Node(head.val, None, None)
            seen[head] = result.next
            head = head.next
            result = result.next
        head = head2
        result = temp.next
        temp = result
        while result:
            result.random = seen[head.random] if head.random else None
            head = head.next
            result = result.next

        return temp


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        head_copy = head
        while head:
            new_node = Node(head.val, None, None)
            new_node.next = head.next
            head.next = new_node
            head = new_node.next

        head = head_copy
        while head:
            head.next.random = head.random.next if head.random else None
            head = head.next.next

        head = head_copy
        old_list = head
        new_list = head.next
        copy = new_list
        while old_list:
            old_list.next = old_list.next.next
            new_list.next = new_list.next.next if new_list.next else None
            old_list = old_list.next
            new_list = new_list.next
        return copy
