from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
        	return
        q = deque([root])
        while q:
        	node = q.pop()
        	while node:
        		nextLeft = node.left
        		nextRight = node.right
        		node.left = None
        		if nextRight:
        			q.append(nextRight)
        		if nextLeft:
        			node.right = nextLeft
        		elif q:
        			node.right = q[-1]
        		node = nextLeft
