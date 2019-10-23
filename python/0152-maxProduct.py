class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        negative, positive = [0] * len(nums), [0] * len(nums)
        if nums[0] > 0:
            positive[0] = nums[0]
        else:
            negative[0] = nums[0]
        maxProduct = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                positive[i] = max(positive[i - 1], 1) * nums[i]
                negative[i] = negative[i - 1] * nums[i]
            else:
                negative[i] = max(positive[i - 1], 1) * nums[i]
                positive[i] = negative[i - 1] * nums[i]
            maxProduct = max(maxProduct, positive[i])
        return maxProduct