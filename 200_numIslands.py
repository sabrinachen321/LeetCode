class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def DFS(grid, i, j):
        	grid[i][j] = '2'
        	for a, b in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        		if 0 <= i + a < len(grid) and 0 <= j + b < len(grid[i]) and grid[i + a][j + b] == '1':
        			DFS(grid, i + a, j + b)

        if not grid or not grid[0]:
        	return 0
        count = 0
        for i in range(len(grid)):
        	for j in range(len(grid[i])):
        		if grid[i][j] == '1':
        			count += 1
        			DFS(grid, i, j)
        for i in range(len(grid)):
        	for j in range(len(grid[i])):
        		if grid[i][j] == '2':
        			grid[i][j] = '1'
        return count
