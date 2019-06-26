from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def recursive(node):
        	if not node:
        		return (True, 0, 0)
        	isLeftValid = isRightValid = True
        	leftMin = rightMax = node.val
        	if node.left:
        		(isLeftValid, leftMin, leftMax) = recursive(node.left)
        		if leftMax >= node.val:
        			return (False, 0, 0)
        	if node.right:
        		(isRightValid, rightMin, rightMax) = recursive(node.right)
        		if rightMin <= node.val:
        			return (False, 0, 0)
        	return (isLeftValid and isRightValid, leftMin, rightMax)

        def iterative(root):
        	node = root
        	preNode = None
        	q = deque([])
        	while node or q:
        		while node:
        			q.append(node)
        			node = node.left
        		node = q.pop()
        		if preNode and preNode.val >= node.val:
        			return False
        		preNode = node
        		node = node.right
        	return True

        return iterative(root)
