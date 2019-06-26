class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ret = [0] * len(queries)
        s = 0
        for a in A:
        	if a % 2 == 0:
        		s += a
        for i in range(len(queries)):
        	q = queries[i][0]
        	index = queries[i][1]
        	a = A[index]
        	if a % 2 == 0:
        		if q % 2 == 0:
        			ret[i] = s = s + q
        		else:
        			ret[i] = s = s - a
        	else:
        		if q % 2 == 0:
        			ret[i] = s
        		else:
        			ret[i] = s = s + a + q
        	A[index] += q
        return ret
