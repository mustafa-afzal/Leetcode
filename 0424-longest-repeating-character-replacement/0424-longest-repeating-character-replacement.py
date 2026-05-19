class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        dict1 = {}
        for r in range(len(s)):
            if s[r] in dict1:
                dict1[s[r]] += 1
            else:
                dict1[s[r]] = 1
            windowSize = r - l + 1
            maxFreq = max(dict1.values())
            if windowSize - maxFreq > k:
                dict1[s[l]] -= 1
                l += 1
            else:
                res = max(res, windowSize)
        return res
