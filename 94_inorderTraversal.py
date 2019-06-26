from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = deque([])
        q = deque([])
        node = root
        while q or node:
        	while node:
        		q.append(node)
        		node = node.left
        	node = q.pop()
        	ret.append(node.val)
        	node = node.right
        return ret
