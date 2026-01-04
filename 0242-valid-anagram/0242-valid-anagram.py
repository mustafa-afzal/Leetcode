class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        dictT = {}
        for i in range(len(s)):
            if s[i] in dictS:
                dictS[s[i]] += 1
            else:
                dictS[s[i]] = 1
        for j in range(len(t)):
            if t[j] in dictT:
                dictT[t[j]] += 1
            else:
                dictT[t[j]] = 1
        if dictS == dictT:
            return True
        return False
