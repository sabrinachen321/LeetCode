from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        q = deque([])
        node = root
        s = 0
        while q or node:
        	while node:
        		q.append(node)
        		node = node.right
        	node = q.pop()
        	node.val += s
        	s = node.val
        	node = node.left
        return root
