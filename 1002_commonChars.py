from collections import Counter

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        dic = Counter(A[0])
        for i in range(1, len(A)):
        	count = Counter(A[i])
        	commonKeys = set(dic.keys()) & set(count.keys())
        	tmpDic = {}
        	for k in commonKeys:
        		tmpDic[k] = min(dic[k], count[k])
        	dic = tmpDic
        ret = []
        for k in dic.keys():
        	for t in range(0, dic[k]):
        		ret.append(k)
        return ret
