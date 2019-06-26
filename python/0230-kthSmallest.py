from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        node = root
        q = deque([])
        index = 0
        while node or q:
        	while node:
        		q.append(node)
        		node = node.left
        	node = q.pop()
        	index += 1
        	if index == k:
        		return node.val
        	node = node.right
        return 0
