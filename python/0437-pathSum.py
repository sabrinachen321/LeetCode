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
        :rtype: int
        """
        def preorder(node, path):
        	if not node:
        		return
        	path.append(node.val)
        	s = 0
        	for p in reversed(path):
        		s += p
        		if s == sumRes:
        			self.res += 1
        	preorder(node.left, path)
        	preorder(node.right, path)
        	path.pop()

        self.res = 0
        preorder(root, [])
        return self.res