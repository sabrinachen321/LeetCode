class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        dayMinute = 60 * 24
        minDiff = dayMinute
        n = len(timePoints)
        for i in range(n):
            curTime = timePoints[i].split(":")
            timePoints[i] = int(curTime[0]) * 60 + int(curTime[1])
        for i in range(n):
            curMinute = timePoints[i]
            prevMinute = timePoints[(n-1) if i == 0 else (i-1)]
            diff = (curMinute + dayMinute - prevMinute) if curMinute < prevMinute else (curMinute - prevMinute)
            minDiff = min(diff, minDiff)
        return minDiff