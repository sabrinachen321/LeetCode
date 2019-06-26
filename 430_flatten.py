from collections import deque

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        newHead = Node(-1, None, None, None)
        newNode = newHead
        q = deque([])
        node = head
        while node or q:
            if not node:
                node = q.pop()
            newNode.next = node
            node.prev = newNode
            if node.child:
                if node.next:
                    q.append(node.next)
                nodeChild = node.child
                node.child = None
                node = nodeChild
            else:
                node = node.next
            newNode = newNode.next
        newHead = newHead.next
        if newHead:
            newHead.prev = None
        return newHead
