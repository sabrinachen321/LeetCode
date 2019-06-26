class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        if (length == 0):
            return []
        count1, count2 = 0, 0
        majority1, majority2 = nums[0], nums[0]
        for num in nums:
            if num == majority1:
                count1 = count1 + 1
            elif num == majority2:
                count2 = count2 + 1 
            elif count1 == 0:
                majority1, count1 = num, 1
            elif count2 == 0:
                majority2, count2 = num, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        res = []
        if nums.count(majority1) > (length / 3):
            res.append(majority1)
        if majority1 != majority2 and nums.count(majority2) > (length / 3):
            res.append(majority2)
        return res
            