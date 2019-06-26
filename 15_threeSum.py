class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        nums.sort()
        l = len(nums)
        for i in range(0, l - 2):
        	if i > 0 and nums[i - 1] == nums[i]:
        		continue
        	j = i + 1
        	k = l - 1
        	while j < k:
        		s = nums[i] + nums[j] + nums[k]
        		if s < 0:
        			j += 1
        		elif s > 0:
        			k -= 1
        		else:
        			ret.append([nums[i], nums[j], nums[k]])
        			while j < k and nums[j] == nums[j + 1]:
        				j += 1
        			while j < k and nums[k] == nums[k - 1]:
        				k -= 1
        			j += 1
        			k -= 1
        return ret
