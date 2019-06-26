from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        curLevel = deque([root])
        backward = False
        while curLevel:
        	nextLevel = deque([])
        	ret.append([])
        	while curLevel:
        		node = curLevel.pop()
        		if node:
        			ret[-1].append(node.val)
        			if backward:
        				nextLevel.append(node.right)
        				nextLevel.append(node.left)
        			else:
        				nextLevel.append(node.left)
        				nextLevel.append(node.right)
        	curLevel = nextLevel
        	backward = not backward
        ret.pop()
        return ret
