class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, (len(nums) - 1)
        while left <= right:
        	if nums[left] <= nums[right]:
        		return nums[left]
        	half = (left + right) / 2
        	if nums[left] <= nums[half]:
        		left = half + 1
        	elif half == 0 or nums[half - 1] > nums[half]:
        		return nums[half]
        	else:
        		right = half - 1