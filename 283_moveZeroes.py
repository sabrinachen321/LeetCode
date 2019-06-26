class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        for num in nums:
        	if num != 0:
        		nums[i] = num
        		i += 1
        for i in range(i, len(nums)):
        	nums[i] = 0
