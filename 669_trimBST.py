# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        while root and not L <= root.val <= R:
        	if root.val < L:
        		root = root.right
        	elif R < root.val:
        		root = root.left
        parent, node = None, root
        while node:
        	if node.val >= L:
        		parent = node
        		node = node.left
        	else:
        		if parent:
        			parent.left = node.right
        		node = node.right
        parent, node = None, root
        while node:
        	if node.val <= R:
        		parent = node
        		node = node.right
        	else:
        		if parent:
        			parent.right = node.left
        		node = node.left
        return root
