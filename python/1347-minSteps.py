class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sMap = self.countFrequency(s)
        tMap = self.countFrequency(t)
        count = 0
        for tChar in tMap.keys():
            count += tMap[tChar] if tChar not in sMap else max(tMap[tChar] - sMap[tChar], 0)
        return count
        
    
    def countFrequency(self, string: str):
        stringMap = {}
        for _, character in enumerate(string):
            stringMap[character] = (stringMap[character] + 1) if character in stringMap else 1
        return stringMap