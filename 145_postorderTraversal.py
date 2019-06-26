from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def recursive(node):
        	if not node:
        		return
        	recursive(node.left)
        	recursive(node.right)
        	self.ret.append(node.val)

        def iterative(root):
        	q = deque([])
        	visited = {}
        	node = root
        	while q or node:
        		while node:
        			q.append(node)
        			node = node.left
        		node = q[-1]
        		if not node.right or (visited.has_key(node) and visited[node]):
        			self.ret.append(node.val)
        			q.pop()
        			node = None
        		else:
        			visited[node] = True
        			node = node.right

        self.ret = []
        iterative(root)
        return self.ret
