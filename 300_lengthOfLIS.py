class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def nn(nums):
        	curLen = [1] * len(nums)
        	glabolMax = 0
        	for i in range(0, len(nums)):
        		for j in range(0, i):
        			if nums[i] > nums[j]:
        				curLen[i] = max(curLen[i], curLen[j] + 1)
        		glabolMax = max(glabolMax, curLen[i])
        	return glabolMax

        def nlogn(nums):
        	dp = []
        	for i in range(0, len(nums)):
        		length = len(dp)
        		if length== 0 or dp[length - 1] < nums[i]:
        			dp.append(nums[i])
        		elif nums[i] <= dp[0]:
        			dp[0] = nums[i]
        		else:
        			s, e = 0, length - 1
        			while s <= e:
        				h = (s + e) / 2
        				if dp[h] < nums[i]:
        					s = h + 1
        				elif dp[h] == nums[i] or dp[h - 1] < nums[i] < dp[h]:
        					dp[h] = nums[i]
        					break
        				else:
        					e = h - 1
        	return len(dp)

        return nlogn(nums)
