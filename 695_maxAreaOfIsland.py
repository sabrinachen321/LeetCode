class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def DFS(grid, i, j, size):
        	grid[i][j] = 2
        	size += 1
        	for a, b in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        		if 0 <= i + a < len(grid) and 0 <= j + b < len(grid[i]) and grid[i + a][j + b] == 1:
        			size = DFS(grid, i + a, j + b, size)
        	return size

        maxSize = 0
        for i in range(len(grid)):
        	for j in range(len(grid[i])):
        		if grid[i][j] == 1:
        			maxSize = max(maxSize, DFS(grid, i, j, 0))
        return maxSize
