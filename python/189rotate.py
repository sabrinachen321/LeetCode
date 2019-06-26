class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if k == 0 or k % length == 0:
        	return
        k = k % length
        start = 0
        curVal = nums[0]
        nextPosition = k
        steps = 0
        while steps < length:
        	steps += 1
        	tmp = nums[nextPosition]
        	nums[nextPosition] = curVal
        	curVal = tmp
        	if nextPosition == start:
        		start += 1
        		curVal = nums[start]
        		nextPosition = start + k
        	else:
        		nextPosition = (nextPosition + k) % length
