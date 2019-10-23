class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output, reverseOutput = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            output[i] = output[i - 1] * nums[i - 1]
        for i in reversed(range(0, len(nums) - 1)):
            reverseOutput[i] = reverseOutput[i + 1] * nums[i + 1]
            output[i] *= reverseOutput[i]
        return output