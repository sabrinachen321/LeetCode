from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recursive(node, v):
        	if not node:
        		return
        	v = (v << 1) + node.val
        	if not node.left and not node.right:
        		self.s += v
        		return
        	recursive(node.left, v)
        	recursive(node.right, v)

        self.s = 0
        recursive(root, 0)
        return self.s
