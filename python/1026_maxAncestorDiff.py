# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recursive(node):
        	leftMin = rightMin = 100000
        	leftMax = rightMax = 0
        	if node.left:
        		(leftMin, leftMax) = recursive(node.left)
        		self.maxDiff = max(self.maxDiff, abs(node.val - leftMin), abs(node.val - leftMax))
        	if node.right:
        		(rightMin, rightMax) = recursive(node.right)
        		self.maxDiff = max(self.maxDiff, abs(node.val - rightMin), abs(node.val - rightMax))
        	return (min(leftMin, node.val, rightMin), max(leftMax, node.val, rightMax))

        self.maxDiff = 0
        recursive(root)
        return self.maxDiff

