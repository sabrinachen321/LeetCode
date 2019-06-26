class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = n ^ (n >> 1)
        return n & (n + 1) == 0
