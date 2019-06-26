# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def buildTree(inorder, a, b, postorder, c, d):
        	if b <= a or d <= c:
        		return None
        	root = TreeNode(postorder[d - 1])
        	for i in range(a, b):
        		if inorder[i] == root.val:
        			break
        	leftLength = i - a
        	rightLength = b - 1 - i
        	root.left = buildTree(inorder, a, i, postorder, c, c + leftLength)
        	root.right = buildTree(inorder, i + 1, b, postorder, c + leftLength, d - 1)
        	return root

        return buildTree(inorder, 0, len(inorder), postorder, 0, len(postorder))
