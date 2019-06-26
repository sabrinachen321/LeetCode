from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def inorder(node, nums):
        	if node:
        		inorder(node.left, nums)
        		nums.append(node.val)
        		inorder(node.right, nums)

        nums = []
        inorder(root, nums)
        i = 0
        j = len(nums) - 1
        while i < j:
        	s = nums[i] + nums[j]
        	if s < k:
        		i += 1
        	elif s > k:
        		j -= 1
        	else:
        		return True
        return False
