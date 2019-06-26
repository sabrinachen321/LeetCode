from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def dfs(node, path, res):
        	if not node.left and not node.right:
        		res.append(path + str(node.val))
        		return
        	path = path + str(node.val) + '->'
        	if node.left:
        		dfs(node.left, path, res)
        	if node.right:
        		dfs(node.right, path, res)

        res = []
        if root:
        	dfs(root, "", res)
        return res
