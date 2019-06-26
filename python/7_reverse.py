import math

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        maxint = pow(2, 31) - 1
        minint = pow(-2, 31)
        ret = 0
        if x < 0:
        	divisor = -10
        else:
        	divisor = 10
        while x != 0:
        	digit = x % divisor
        	if ret > (maxint / 10) or (ret == (maxint / 10) and digit > (maxint % 10)):
        	    return 0
        	if ret < int(minint / 10.0) or (ret == int(minint / 10.0) and digit < (minint % -10)):
        		return 0
        	ret = (ret * 10) + digit
        	x = int(x / 10.0)
        return ret

