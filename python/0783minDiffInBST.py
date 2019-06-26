from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        prev = None
        node = root
        q = deque([])
        minDiff = 0x0FFFFFFF
        while node or q:
        	while node:
        		q.append(node)
        		node = node.left
        	node = q.pop()
        	if prev and (node.val - prev.val) < minDiff:
        		minDiff = node.val - prev.val
        	prev = node
        	node = node.right
        return minDiff
