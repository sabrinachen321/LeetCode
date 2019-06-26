"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def recursive(node):
            if not node or (not node.left and not node.right):
                return
            node.left.next = node.right
            if node.next:
                node.right.next = node.next.left
            recursive(node.left)
            recursive(node.right)
            
        recursive(root)
        return root
