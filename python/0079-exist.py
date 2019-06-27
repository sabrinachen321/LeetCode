class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(board, visited, i, j, word, w):
        	if board[i][j] == word[w]:
        		visited[i][j] = True
        		for p in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        			nextI, nextJ = (i + p[0]), (j + p[1])
        			if (w + 1) == len(word) or (0 <= nextI < len(board) and 0 <= nextJ < len(board[i]) and not visited[nextI][nextJ] and dfs(board, visited, nextI, nextJ, word, w + 1)):
        				return True
        		visited[i][j] = False
        	return False

        visited = [[False] * len(board[0]) for i in range(len(board))]
        for i in range(len(board)):
        	for j in range(len(board[i])):
        		if dfs(board, visited, i, j, word, 0):
        			return True
        return False