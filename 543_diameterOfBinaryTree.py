# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def postOrder(node):
        	if not node:
        		return 0
        	leftLength = rightLength = 0
        	if node.left:
        		leftLength += (postOrder(node.left) + 1)
        	if node.right:
        		rightLength += (postOrder(node.right) + 1)
        	self.diameter = max(self.diameter, leftLength + rightLength)
        	return max(leftLength, rightLength)

        self.diameter = 0
        postOrder(root)
        return self.diameter
