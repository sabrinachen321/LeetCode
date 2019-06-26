# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def recursive(node, val):
        	if not node:
        		return TreeNode(val)
        	if val < node.val:
        		node.left = recursive(node.left, val)
        	elif node.val < val:
        		node.right = recursive(node.right, val)
        	return node

        def iterative(root, val):
        	if not root:
        		return TreeNode(val)
        	node = root
        	while node:
        		if val < node.val:
        			if node.left:
        				node = node.left
        			else:
        				node.left = TreeNode(val)
        				break
        		elif node.val < val:
        			if node.right:
        				node = node.right
        			else:
        				node.right = TreeNode(val)
        				break
        	return root

        return iterative(root, val)
