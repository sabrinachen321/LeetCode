from collections import deque

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def recursive(node):
        	if not node:
        		return
        	self.ret.append(node.val)
        	for c in node.children:
        		recursive(c)

        def iterative(root):
        	q = deque([root])
        	while q:
        		node = q.pop()
        		while node:
        			self.ret.append(node.val)
        			if len(node.children) > 0:
        				for i in range(len(node.children) - 1, 0, -1):
        					q.append(node.children[i])
        				node = node.children[0]
        			else:
        				node = None

        self.ret = []
        iterative(root)
        return self.ret
