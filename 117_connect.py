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
        def iterative(root):
            node = root
            while node:
                firstChildNode = preChildNode = None
                nextNode = node
                while nextNode:
                    nextLinkNode = nextPreNode = None
                    if nextNode.left and nextNode.right:
                        nextNode.left.next = nextNode.right
                        nextLinkNode, nextPreNode = nextNode.left, nextNode.right
                    elif nextNode.left:
                        nextLinkNode = nextPreNode = nextNode.left
                    elif nextNode.right:
                        nextLinkNode = nextPreNode = nextNode.right
                    if preChildNode:
                        preChildNode.next = nextLinkNode
                    if nextPreNode:
                        preChildNode = nextPreNode
                    if nextLinkNode and not firstChildNode:
                        firstChildNode = nextLinkNode
                    nextNode = nextNode.next
                node = firstChildNode
            return root

        return iterative(root)
