# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def postOrder(node):
        	if not node:
        		return 0
        	s = postOrder(node.left) + node.val + postOrder(node.right)
        	if not self.count.has_key(s):
        		self.count[s] = 0
        	self.count[s] += 1
        	if self.maxCount <= self.count[s]:
        		if self.maxCount < self.count[s]:
        			self.ret[:] = []
        		self.ret.append(s)
        		self.maxCount = self.count[s]
        	return s

        self.maxCount = 0
        self.count = {}
        self.ret = []
        postOrder(root)
        return self.ret
