# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def postOrder(node):
        	if not node or (not node.left and not node.right):
        		return 0
        	leftLength = postOrder(node.left)
        	rightLength = postOrder(node.right)
        	if node.left and node.val == node.left.val:
        		leftLength += 1
        	else:
        		leftLength = 0
        	if node.right and node.val == node.right.val:
        		rightLength += 1
        	else:
        		rightLength = 0
        	length = max(leftLength, rightLength)
        	self.maxLength = max(self.maxLength, leftLength + rightLength)
        	return length

        self.maxLength = 0
        postOrder(root)
        return self.maxLength
