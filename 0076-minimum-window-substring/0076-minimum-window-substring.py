from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        resL = 0
        resR = 0
        seenS = {}
        seenT = {}
        need = len(set(t))
        have = 0
        minWindowLen = float('inf')
        for i in range(len(t)):
            seenT = Counter(t)
        for r in range(len(s)):
            seenS[s[r]] = seenS.get(s[r], 0) + 1
            if seenT[s[r]] and seenS[s[r]] == seenT[s[r]]:
                have += 1
            while have == need:
                windowLen = r - l + 1
                if windowLen < minWindowLen:
                    minWindowLen = windowLen
                    resL = l
                    resR = r
                seenS[s[l]] = seenS.get(s[l], 0) - 1
                if seenS[s[l]] < seenT[s[l]]:
                    have -= 1
                l += 1
        if minWindowLen == float('inf'):
            return ""
        return s[resL : resR + 1]
                
            
        
        
            
            
