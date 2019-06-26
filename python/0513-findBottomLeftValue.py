from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        first = None
        curLevel = deque([root])
        nextLevel = deque([])
        while curLevel:
        	first = curLevel[0]
        	nextLevel.clear()
        	while curLevel:
        		node = curLevel.popleft()
        		if node.left:
        			nextLevel.append(node.left)
        		if node.right:
        			nextLevel.append(node.right)
        	curLevel.extend(nextLevel)
        return first.val
