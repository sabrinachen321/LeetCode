class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Pn = sum(nums)
        s = 0
        for i in range(0, len(nums)):
            if (s * 2 + nums[i]) == Pn:
                return i
            s += nums[i]
        return -1