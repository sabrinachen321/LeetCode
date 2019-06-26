"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        def postOrder(node):
        	if not node:
        		return 0
        	maxHeight = 0
        	for c in node.children:
        		maxHeight = max(maxHeight, postOrder(c))
        	return maxHeight + 1

        return postOrder(root)
