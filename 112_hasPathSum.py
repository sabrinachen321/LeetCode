from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        q = deque([(root, 0)])
        while q:
        	(node, s) = q.popleft()
        	if not node:
        		continue
        	s += node.val
        	if not node.left and not node.right:
        		if sum == s:
        			return True
        	q.append((node.left, s))
        	q.append((node.right, s))
        return False
