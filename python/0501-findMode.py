# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inOrder(node):
        	if not node:
        		return
        	inOrder(node.left)
        	if self.prev and self.prev.val == node.val:
        		self.count += 1
        	else:
        		self.count = 1
        		self.prev = node
        	if self.count >= self.maxCount:
        		if self.count > self.maxCount:
        			self.ret[:] = []
        		self.ret.append(node.val)
        		self.maxCount = self.count
        	inOrder(node.right)

        self.prev = None
        self.ret = []
        self.maxCount = 0
        inOrder(root)
        return self.ret
