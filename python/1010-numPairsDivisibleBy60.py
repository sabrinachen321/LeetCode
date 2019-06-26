class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        dic = {}
        for t in time:
        	mod = t % 60
        	if dic.has_key(mod):
        		dic[mod] += 1
        	else:
        		dic[mod] = 1
        res = 0
        for k in dic.keys():
        	kp = (60 - k) % 60
        	if dic[k] > 0 and dic.has_key(kp) and dic[kp] > 0:
        		if k != kp:
        			res += dic[k] * dic[kp]
        		else:
        			res += dic[k] * (dic[k] - 1) / 2
        		dic[kp] = 0
        	dic[k] = 0
        return res
