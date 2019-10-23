class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        P = 1
        res = 0
        for (i, num) in enumerate(nums):
            P *= num
            while P >= k and left <= i:
                P /= nums[left]
                left += 1
            res += (i - left + 1)
        return res