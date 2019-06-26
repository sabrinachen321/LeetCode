from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def postOrder(node):
        	if not node:
        		return (0, True)
        	(leftHeight, isLeftBalanced) = postOrder(node.left)
        	if not isLeftBalanced:
        		return (0, False)
        	(rightHeight, isRightBalanced) = postOrder(node.right)
        	if not isRightBalanced:
        		return (0, False)
        	return (max(leftHeight, rightHeight) + 1, abs(leftHeight - rightHeight) <= 1 and isLeftBalanced and isRightBalanced)

        (height, isBalanced) = postOrder(root)
        return isBalanced
