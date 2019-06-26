class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 1
        j = len(numbers)
        while i < j:
            s = numbers[i - 1] + numbers[j - 1]
            if s < target:
                i += 1
            elif s > target:
                j -= 1
            else:
                return [i, j]
