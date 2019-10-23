from collections import Counter

class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        subSum = [0] * (len(A) + 1)
        for i in range(0, len(A)):
            subSum[i + 1] = (subSum[i] + A[i]) % K
        count = Counter(subSum)
        return sum((v * (v - 1) / 2) for v in count.values())