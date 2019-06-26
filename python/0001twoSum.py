class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = { }
        for i, element in enumerate(nums):
            sub = target - element
            if dictionary.has_key(sub):
                return { dictionary[sub], i }
            dictionary[element] = i
        