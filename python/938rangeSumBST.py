# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        def recursive(node, L, R):
        	if not node:
        		return 0
        	leftSum = rightSum = selfRes = 0
        	if node.val > L:
        		leftSum = recursive(node.left, L, R)
        	if node.val < R:
        		rightSum = recursive(node.right, L, R)
        	if L <= node.val <= R:
        		selfRes = node.val
        	return leftSum + rightSum + selfRes

        return recursive(root, L, R)
