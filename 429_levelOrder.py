from collections import deque

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        ret = []
        if not root:
        	return ret
        curLevel = deque([root])
        while curLevel:
        	ret.append([])
        	nextLevel = deque([])
        	while curLevel:
        		node = curLevel.popleft()
        		if node:
        			ret[-1].append(node.val)
        			for c in node.children:
        				nextLevel.append(c)
        	curLevel = nextLevel
        return ret