from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
        	return -1
        smallest = root.val
        potential = -1
        q = deque([root])
        while q:
        	node = q.pop()
        	if node.left:
        		if node.left.val > smallest:
        			if node.left.val < potential or potential == -1:
        				potential = node.left.val
        		else:
        			q.append(node.left)
        	if node.right:
        		if node.right.val > smallest:
        			if node.right.val < potential or potential == -1:
        				potential = node.right.val
        		else:
        			q.append(node.right)
        return potential

