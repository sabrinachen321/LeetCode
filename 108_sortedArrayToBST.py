# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def buildNode(start, end):
        	if start > end:
        		return None
        	half = (start + end) / 2
        	node = TreeNode(nums[half])
        	node.left = buildNode(start, half - 1)
        	node.right = buildNode(half + 1, end)
        	return node

        return buildNode(0, len(nums) - 1)
