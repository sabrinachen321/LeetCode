from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def recursive(node):
        	if not node:
        		return
        	self.ret.append(node.val)
        	recursive(node.left)
        	recursive(node.right)

        def iterative(root):
        	q = deque([root])
        	while q:
        		node = q.pop()
        		while node:
        			self.ret.append(node.val)
        			q.append(node.right)
        			node = node.left

        self.ret = []
        iterative(root)
        return self.ret
