# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def postOrder(node):
        	if not node:
        		return 0
        	leftSum = postOrder(node.left)
        	rightSum = postOrder(node.right)
        	self.maxSum = max(self.maxSum, max(0, leftSum) + node.val + max(0, rightSum))
        	return max(max(leftSum, rightSum), 0) + node.val

        self.maxSum = -sys.maxint - 1
        postOrder(root)
        return self.maxSum
