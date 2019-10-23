from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        subSum = [0] * (len(nums) + 1)
        for i in range(0, len(nums)):
            subSum[i + 1] = subSum[i] + nums[i]
        count = defaultdict(int)
        res = 0
        for sub in subSum:
            res += count[sub - k]
            count[sub] += 1
        return res