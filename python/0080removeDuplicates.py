class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        l = len(nums)
        for j in range(l):
        	if not (i > 1 and nums[j] == nums[i - 1] and nums[j] == nums[i - 2]):
        		nums[i] = nums[j]
        		i += 1
        return i

