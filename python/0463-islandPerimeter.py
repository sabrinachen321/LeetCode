import Queue

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        length = len(grid)
        width = len(grid[0])

        isVisited = [[False] * width for i in range(length)]
        q = Queue.Queue()
        [i, j] = self.findFirst(grid)
        q.put([i, j])
        isVisited[i][j] = True
        
        perimeter = 0
        while not q.empty():
        	cell = q.get()
        	i = cell[0]
        	j = cell[1]
        	perimeter = perimeter + 4
        	for [a, b] in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        		if (i + a) >= 0 and (i + a) < length and (j + b) >= 0 and (j + b) < width and grid[i + a][j + b] == 1:
        			perimeter -= 1
        			if not isVisited[i + a][j + b]:
        				q.put([i + a, j + b])
        				isVisited[i + a][j + b] = True
        return perimeter

    def findFirst(self, grid):
    	for i in range(0, len(grid)):
        	for j in range(0, len(grid[i])):
        		if grid[i][j] == 1:
        			return [i, j]
