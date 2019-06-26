class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ss = s.lower()
        s, e = 0, len(ss) - 1
        while s < e:
        	if ord(ss[s]) not in range(ord('a'), ord('z') + 1) and ord(ss[s]) not in range(ord('0'), ord('9') + 1):
        		s += 1
        	elif ord(ss[e]) not in range(ord('a'), ord('z') + 1) and ord(ss[e]) not in range(ord('0'), ord('9') + 1):
        		e -= 1
        	elif ss[s] != ss[e]:
        		return False
        	else:
        		s += 1
        		e -= 1
        return True
