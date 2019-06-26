# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def height(node, isRight):
        	if not node:
        		return -1
        	if isRight:
        		return 1 + height(node.right, isRight)
        	else:
        		return 1 + height(node.left, isRight)

        def count(node):
        	leftH = height(node, False)
        	rightH = height(node, True)
        	if leftH == rightH:
        		if leftH == -1:
        			return 0
        		else:
        			return pow(2, leftH + 1) - 1
        	else:
        		return 1 + count(node.left) + count(node.right)

        return count(root)
