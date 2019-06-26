from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
        	node = TreeNode(v)
        	node.left = root
        	return node
        curLevel = deque([root])
        nextLevel = deque([])
        levelIndex = 1
        while levelIndex < (d - 1):
        	nextLevel.clear()
        	while curLevel:
        		node = curLevel.popleft()
        		if node.left:
        			nextLevel.append(node.left)
        		if node.right:
        			nextLevel.append(node.right)
        	curLevel.extend(nextLevel)
        	levelIndex += 1
        for node in curLevel:
        	originLeft = node.left
        	originRight = node.right
        	node.left = TreeNode(v)
        	node.right = TreeNode(v)
        	node.left.left = originLeft
        	node.right.right = originRight
        return root