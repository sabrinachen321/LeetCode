# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def postOrder(node):
        	if not node:
        		return 0
        	return max(postOrder(node.left), postOrder(node.right)) + 1

        return postOrder(root)
