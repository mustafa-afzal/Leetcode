class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        for i in range(len(s)):
            if s[i] in dictS:
                dictS[s[i]] += 1
            else:
                dictS[s[i]] = 1
        dictT = {}
        for j in range(len(t)):
            if t[j] in dictT:
                dictT[t[j]] += 1
            else:
                dictT[t[j]] = 1
        return dictS == dictT