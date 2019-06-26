class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start, end = 0, len(s) - 1
        diffS, diffE = -1, -1
        while start < end:
        	if s[start] == s[end]:
        		start += 1
        		end -= 1
        	elif diffS == -1:
        		diffS = start
        		start += 1
        	elif diffE == -1:
        		start = diffS
        		diffE = len(s) - 1 - diffS
        		end = diffE - 1
        	else:
        		return False
        return True