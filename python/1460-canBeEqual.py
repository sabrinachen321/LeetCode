class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        targetMap = {}
        for _, t in enumerate(target):
            targetMap[t] = 1 if t not in targetMap else (targetMap[t] + 1)
        for _, a in enumerate(arr):
            if a not in targetMap:
                return False
            targetMap[a] -= 1
            if targetMap[a] < 0:
                return False
        return True