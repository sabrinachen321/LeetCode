from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def recursive(node, val):
        	if not node:
        		return None
        	elif node.val == val:
        		return node
        	elif val < node.val:
        		return recursive(node.left, val)
        	else:
        		return recursive(node.right, val)

        def iterative(root, val):
        	q = deque([root])
        	while q:
        		node = q.pop()
        		if node:
        			if node.val == val:
        				return node
        			elif val < node.val:
        				q.append(node.left)
        			else:
        				q.append(node.right)
        		else:
        			return None
        	return None

        return iterative(root, val)
