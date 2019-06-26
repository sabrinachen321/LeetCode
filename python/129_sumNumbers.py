# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def preOrder(node, number):
        	if not node:
        		return
        	number = number * 10 + node.val
        	if not node.left and not node.right:
        		self.s += number
        	preOrder(node.left, number)
        	preOrder(node.right, number)

        self.s = 0
        preOrder(root, 0)
        return self.s
