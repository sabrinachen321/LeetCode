# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def postOrder(node):
        	if not node:
        		return 0
        	leftSum = postOrder(node.left)
        	rightSum = postOrder(node.right)
        	self.tilt += abs(leftSum - rightSum)
        	return leftSum + node.val + rightSum

        self.tilt = 0
        postOrder(root)
        return self.tilt
