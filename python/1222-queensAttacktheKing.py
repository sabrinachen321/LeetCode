class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        direction = {}
        for queen in queens:
            if queen[0] == king[0]:
                if queen[1] < king[1] and (1 not in direction or direction[1][1] < queen[1]):
                    direction[1] = queen
                elif queen[1] > king[1] and (2 not in direction or direction[2][1] > queen[1]):
                    direction[2] = queen
            elif queen[1] == king[1]:
                if queen[0] < king[0] and (3 not in direction or direction[3][0] < queen[0]):
                    direction[3] = queen
                elif queen[0] > king[0] and (4 not in direction or direction[4][0] > queen[0]):
                    direction[4] = queen
            elif (queen[0] - king[0]) == (queen[1] - king[1]) < 0 and (5 not in direction or direction[5][0] < queen[0]):
                direction[5] = queen
            elif 0 < (queen[0] - king[0]) == (queen[1] - king[1]) and (6 not in direction or direction[6][0] > queen[0]):
                direction[6] = queen
            elif 0 < (queen[0] - king[0]) == (king[1] - queen[1]) and (7 not in direction or direction[7][0] > queen[0]):
                direction[7] = queen
            elif (queen[0] - king[0]) == (king[1] - queen[1]) < 0 and (8 not in direction or direction[8][0] < queen[0]):
                direction[8] = queen
        return direction.values()