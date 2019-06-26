# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def copyTree(root, valIncrement):
        	if not root:
        		return None
        	node = TreeNode(root.val + valIncrement)
        	node.left = copyTree(root.left, valIncrement)
        	node.right = copyTree(root.right, valIncrement)
        	return node

        if n == 0:
        	return []
        treesOfNode = [[] for i in range(n + 1)]
        treesOfNode[0].append(None)
        for i in range(1, n + 1):
        	for j in range(1, i + 1):
        		for leftTree in treesOfNode[j - 1]:
        			for rightTree in treesOfNode[i - j]:
        				root = TreeNode(j)
        				root.left = leftTree
        				root.right = copyTree(rightTree, j)
        				treesOfNode[i].append(root)
        return treesOfNode[n]
