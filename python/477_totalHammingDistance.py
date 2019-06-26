import math

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maxint = pow(10, 9)
        mask = 1
        while maxint != 0:
            oneCount = 0
            zeroCount = 0
            for n in nums:
                if (n & mask) != 0:
                    oneCount = oneCount + 1
                else:
                    zeroCount = zeroCount + 1
            count = count + oneCount * zeroCount
            maxint = maxint >> 1
            mask = mask << 1
        return count
