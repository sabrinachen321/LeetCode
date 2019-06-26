from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        trees = defaultdict()
        trees.default_factory = trees.__len__
        count = defaultdict(int)
        res = []

        def lookup(node):
        	if node:
        		uid = trees[(node.val, lookup(node.left), lookup(node.right))]
        		if count[uid] == 1:
        			res.append(node)
        		count[uid] += 1
        		return uid

        lookup(root)
        return res
