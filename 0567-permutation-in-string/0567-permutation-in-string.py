from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1 = Counter(s1)
        k = len(s1)
        map2 = Counter(s2[:k])
        if map1 == map2:
            return True
        for i in range(0, len(s2) - k):
            map2[s2[i]] -= 1
            if map2[s2[i]] == 0:
                del map2[s2[i]]
            map2[s2[i + k]] += 1
            if map1 == map2:
                return True
        return False