from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        curLevel = deque([root])
        while curLevel:
        	nextLevel = deque([])
        	foundX = foundY = False
        	while curLevel:
        		node = curLevel.popleft()
        		if node:
        			if node.left and node.right and ((node.left.val == x and node.right.val == y) or (node.left.val == y and node.right.val == x)):
        				return False
        			if node.left:
        				if node.left.val == x:
        					foundX = True
        				if node.left.val == y:
        					foundY = True
        			if node.right:
        				if node.right.val == x:
        					foundX = True
        				if node.right.val == y:
        					foundY = True
        			nextLevel.append(node.left)
        			nextLevel.append(node.right)
        	if foundX and foundY:
        		return True
        	curLevel = nextLevel
        return False
