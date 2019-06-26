class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums or not nums[0] or len(nums) * len(nums[0]) != r * c:
        	return nums
        ro = len(nums)
        co = len(nums[0])
        newNums = [[0] * c for i in range(r)]
        for i in range(r * c):
        	newNums[int(i / c)][i % c] = nums[int(i / co)][i % co]
        return newNums
