class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] < nums[right]:
                return nums[left]
            half = (left + right) / 2
            if left == right == 0 or nums[half - 1] > nums[half]:
                return nums[half]
            if nums[left] == nums[half] == nums[right]:
                for i in range(left, right + 1):
                    if i > 0 and nums[i - 1] > nums[i]:
                        return nums[i]
                return nums[left]
            if nums[left] < nums[half] or nums[half] > nums[right]:
                left = half + 1
            elif nums[half] < nums[right] or nums[left] > nums[half]:
                right = half - 1