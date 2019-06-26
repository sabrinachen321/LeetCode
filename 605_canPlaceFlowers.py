class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed.insert(0, 1)
        flowerbed.insert(1, 0)
        flowerbed.append(0)
        flowerbed.append(1)
        continuesN = 0
        total = 0
        for bed in flowerbed:
        	if bed == 1:
        		if continuesN > 2:
        			total += (continuesN - 1) / 2
        		continuesN = 0
        	else:
        		continuesN += 1
        return total >= n
