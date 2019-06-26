from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        curLevel = deque([root])
        while curLevel:
        	ret.append([])
        	nextLevel = deque([])
        	while curLevel:
        		node = curLevel.popleft()
        		if node:
        			ret[-1].append(node.val)
        			nextLevel.append(node.left)
        			nextLevel.append(node.right)
        	curLevel = nextLevel
        ret.pop()
        return ret
