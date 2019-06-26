from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def preOrder(node):
        	if not node:
        		return
        	originalLeft = node.left
        	node.left = node.right
        	node.right = originalLeft
        	preOrder(node.left)
        	preOrder(node.right)

        def iterative(node):
        	q = deque([node])
        	while q:
        		node = q.popleft()
        		while node:
        			originalLeft = node.left
        			node.left = node.right
        			node.right = originalLeft
        			if node.left:
        				q.append(node.left)
        			node = node.right

        iterative(root)
        return root
