from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        parent, node = None, root
        while node:
        	if node.val == key:
        		break
        	else:
        		parent = node
        		if key < node.val:
        			node = node.left
        		else:
        			node = node.right
        if not node:
        	return root
        nodeLeft, nodeRight = node.left, node.right
        replaceParent = node
        if not node.left and not node.right:
        	replacement = None
        elif node.left:
        	replacement = node.left
        	while replacement.right:
        		replaceParent = replacement
        		replacement = replacement.right
        	replaceParent.right = replacement.left
        else:
        	replacement = node.right
        	while replacement.left:
        		replaceParent = replacement
        		replacement = replacement.left
        	replaceParent.left = replacement.right
        if replacement:
        	if replacement != nodeLeft:
        		replacement.left = nodeLeft
        	if replacement != nodeRight:
        		replacement.right = nodeRight
        if parent:
        	if node.val < parent.val:
        		parent.left = replacement
        	else:
        		parent.right = replacement
        	return root
        else:
        	return replacement