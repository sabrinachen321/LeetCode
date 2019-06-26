from collections import deque

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        q = deque([(sr, sc)])
        oldColor = image[sr][sc]
        while q:
        	i, j = q.popleft()
        	if image[i][j] == newColor:
        		continue
        	image[i][j] = newColor
        	for a, b in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        		if 0 <= i + a < len(image) and 0 <= j + b < len(image[i]) and image[i + a][j + b] == oldColor:
        			q.append((i + a, j + b))
        return image
