# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def buildTree(preorder, a, b, inorder, c, d):
        	if b <= a or d <= c:
        		return None
        	root = TreeNode(preorder[a])
        	for i in range(c, d):
        		if preorder[a] == inorder[i]:
        			break
        	leftLength = i - c
        	rightLength = d - i - 1
        	root.left = buildTree(preorder, a + 1, a + 1 + leftLength, inorder, c, i)
        	root.right = buildTree(preorder, a + 1 + leftLength, b, inorder, i + 1, d)
        	return root

        length = len(preorder)
        return buildTree(preorder, 0, length, inorder, 0, length)
