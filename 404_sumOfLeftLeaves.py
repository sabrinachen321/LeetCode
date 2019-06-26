from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = deque([root])
        s = 0
        while q:
        	node = q.pop()
        	while node:
        		if node.left and not node.left.left and not node.left.right:
        			s += node.left.val
        		q.append(node.right)
        		node = node.left
        return s
