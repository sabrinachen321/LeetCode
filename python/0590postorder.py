from collections import deque

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def recursive(node):
        	if not node:
        		return
        	for c in node.children:
        		recursive(c)
        	self.ret.append(node.val)

        def iterative(root):
        	q = deque([])
        	visited = {}
        	node = root
        	while q or node:
        		while node:
        			q.append(node)
        			visited[node] = 1
        			if len(node.children) > 0:
        				node = node.children[0]
        			else:
        				node = None
        		node = q[-1]
        		if visited[node] >= len(node.children):
        			self.ret.append(node.val)
        			q.pop()
        			node = None
        		else:
        			nextChild = node.children[visited[node]]
        			visited[node] += 1
        			node = nextChild

        self.ret = []
        iterative(root)
        return self.ret
