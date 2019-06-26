from collections import deque

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
        	return
        q = deque([])
        for i in range(len(board)):
        	for j in [0, len(board[0]) - 1]:
        		if board[i][j] == 'O':
        			q.append((i, j))
        for i in [0, len(board) - 1]:
        	for j in range(1, len(board[i]) - 1):
        		if board[i][j] == 'O':
        			q.append((i, j))
        while q:
        	i, j = q.popleft()
        	board[i][j] = 'A'
        	for a, b in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        		if 0 <= (i + a) < len(board) and 0 <= (j + b) < len(board[0]) and board[i + a][j + b] == 'O':
        			q.append((i + a, j + b))
        for i in range(len(board)):
        	for j in range(len(board[i])):
        		if board[i][j] == 'O':
        			board[i][j] = 'X'
        		elif board[i][j] == 'A':
        			board[i][j] = 'O'

