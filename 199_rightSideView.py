from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if not root:
        	return ret
        curLevel = deque([root])
        while curLevel:
        	nextLevel = deque([])
        	ret.append(curLevel[0].val)
        	while curLevel:
        		node = curLevel.popleft()
        		if node.right:
        			nextLevel.append(node.right)
        		if node.left:
        			nextLevel.append(node.left)
        	curLevel = nextLevel
        return ret
