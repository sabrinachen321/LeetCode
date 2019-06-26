import math

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        isPrime = [True] * (n)
        isPrime[0] = isPrime[1] = False
        for i in range(2, int(math.sqrt(n)) + 1):
        	if isPrime[i]:
        		for j in range(i, int(math.ceil(float(n) / i))):
        			isPrime[i * j] = False
        return isPrime.count(True)
