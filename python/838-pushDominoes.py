class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        length = len(dominoes)
        lTime = [0 for i in range(length)]
        rTime = [0 for i in range(length)]
        for i in range(length):
            if dominoes[i] == '.' and i > 0 and (dominoes[i-1] == 'R' or rTime[i-1] > 0):
                rTime[i] = rTime[i-1] + 1
        for i in reversed(range(length)):
            if dominoes[i] == '.' and i < (length-1) and (dominoes[i+1] == 'L' or lTime[i+1] > 0):
                lTime[i] = lTime[i+1] + 1
        
        dList = list(dominoes)
        for i in range(length):
            if dList[i] == '.' and lTime[i] != rTime[i]:
                if lTime[i] == 0 or (0 < rTime[i] < lTime[i]):
                    dList[i] = 'R'
                elif rTime[i] == 0 or (0 < lTime[i] < rTime[i]):
                    dList[i] = 'L'
        return ''.join(dList)