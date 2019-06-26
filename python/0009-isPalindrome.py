class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
        	return False
        t = x
        h = 1
        while (t / h) >= 10:
        	h *= 10
        while h > 0:
        	head = x / h
        	tail = x % 10
        	print head, tail
        	if head != tail:
        		return False
        	x -= h * head
        	x /= 10
        	h /= 100
        return True