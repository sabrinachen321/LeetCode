from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sumRes):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def preorder(node, path, ret):
        	if not node:
        		return
        	path.append(node.val)
        	if not node.left and not node.right:
        		if sum(path) == sumRes:
        			ret.append(copy.copy(path))
        	preorder(node.left, path, ret)
        	preorder(node.right, path, ret)
        	path.pop()

        ret = []
        preorder(root, deque([]), ret)
        return ret
