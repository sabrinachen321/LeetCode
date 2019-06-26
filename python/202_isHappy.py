class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def compute(n):
        	s = 0
        	while n:
        		digit = n % 10
        		s += (digit * digit)
        		n /= 10
        	return s

        interSet = set([])
        nextNum = compute(n)
        while nextNum not in interSet and nextNum != 1:
        	interSet.add(nextNum)
        	nextNum = compute(nextNum)
        if nextNum == 1:
        	return True
        return False
