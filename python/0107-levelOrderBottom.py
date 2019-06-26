from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = deque([])
        curLevel = deque([root])
        while curLevel:
        	ret.appendleft([])
        	nextLevel = deque([])
        	while curLevel:
        		node = curLevel.popleft()
        		if node:
        			ret[0].append(node.val)
        			nextLevel.append(node.left)
        			nextLevel.append(node.right)
        	curLevel = nextLevel
        ret.popleft()
        return ret
