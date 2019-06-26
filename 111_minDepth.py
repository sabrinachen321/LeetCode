# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def postOrder(node):
        	if not node:
        		return 99999999
        	if not node.left and not node.right:
        		return 1
        	return min(postOrder(node.left), postOrder(node.right)) + 1

        if not root:
        	return 0
        return postOrder(root)
