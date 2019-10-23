class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = nums[0]
        maxSub = [nums[0]] * len(nums)
        for i in range(1, len(nums)): 
            maxSub[i] = nums[i] + (maxSub[i - 1] if maxSub[i - 1] > 0 else 0)
            maxSum = max(maxSum, maxSub[i])
        return maxSum