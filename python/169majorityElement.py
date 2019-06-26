class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for num in nums:
            if count == 0:
                majority = num
            elif majority != num:
                count = count - 1
                continue
            count = count + 1
        return majority