class Solution(object):
    def countBit(self, n):
    	count = 0
    	while n != 0:
    		count = count + 1
    		n = n & (n - 1)
    	return count

    
    def isPrimeNumber(self, n):
    	primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    	return n in primes
    
    
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        count = 0;
        for n in range(L, R + 1):
        	if self.isPrimeNumber(self.countBit(n)):
        		count = count + 1
        return count
