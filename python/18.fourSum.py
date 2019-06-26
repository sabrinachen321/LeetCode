class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ret = []
        l = len(nums)
        for i in range(0, l - 3):
        	if i > 0 and nums[i - 1] == nums[i]:
        		continue
        	for j in range(i + 1, l - 2):
        		if j > i + 1 and nums[j - 1] == nums[j]:
        			continue
        		k = j + 1
        		m = l - 1
        		while k < m:
        			s = nums[i] + nums[j] + nums[k] + nums[m]
        			if s < target:
        				k += 1
        			elif s > target:
        				m -= 1
        			else:
        				ret.append([nums[i], nums[j], nums[k], nums[m]])
        				while k < m and nums[k] == nums[k + 1]:
        					k += 1
        				while k < m and nums[m] == nums[m - 1]:
        					m -= 1
        				k += 1
        				m -= 1
        return ret
