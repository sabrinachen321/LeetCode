class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        powOfTwo = 1
        for n in range(1, num + 1):
            if n == powOfTwo:
                res.append(1)
                powOfTwo = powOfTwo * 2
            else:
                res.append(res[n - powOfTwo] + 1)
        return res
