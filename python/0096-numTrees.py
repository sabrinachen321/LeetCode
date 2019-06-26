class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        numOfNodes = [0] * (n + 1)
        numOfNodes[0] = 1
        for i in range(1, n + 1):
        	for j in range(1, i + 1):
        		numOfNodes[i] += numOfNodes[j - 1] * numOfNodes[i - j]
        return numOfNodes[n]
