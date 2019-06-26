from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ret = []
        curLevel = deque([root])
        while curLevel:
        	nextLevel = deque([])
        	s = 0
        	n = 0
        	while curLevel:
        		node = curLevel.popleft()
        		if node:
        			s += node.val
        			n += 1
        			nextLevel.append(node.left)
        			nextLevel.append(node.right)
        	if n > 0:
        		ret.append(float(s) / n)
        	curLevel = nextLevel
        return ret