class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        map1 = {}
        map2 = {}
        k = len(s1)
        for i in range(len(s1)):
            if s1[i] in map1:
                map1[s1[i]] += 1
            else:
                map1[s1[i]] = 1
        for i in range(k):
            if s2[i] in map2:
                map2[s2[i]] += 1
            else:
                map2[s2[i]] = 1
        for i in range(0, len(s2) - k):
            if map1 == map2: return True
            if s2[i+k] in map2:
                map2[s2[i+k]] += 1
            else:
                map2[s2[i+k]] = 1
            map2[s2[i]] -= 1
            if map2[s2[i]] == 0:
                del map2[s2[i]]
        return map1 == map2
