class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            half = (left + right) / 2
            if nums[half] == target:
                return True
            if nums[left] < nums[half] or nums[half] > nums[right]:
                if nums[left] <= target < nums[half]:
                    right = half - 1
                else:
                    left = half + 1
            elif nums[half] < nums[right] or nums[left] > nums[half]:
                if nums[half] < target <= nums[right]:
                    left = half + 1
                else:
                    right = half - 1
            else:
                for i in range(left, right + 1):
                    if nums[i] == target:
                        return True
                return False
        return False