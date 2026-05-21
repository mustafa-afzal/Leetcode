class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        map = {}
        res = 0
        for r in range(len(s)):
            if s[r] in map:
                map[s[r]] += 1
            else:
                map[s[r]] = 1
            maxFreq = max(map.values())
            windowSize = r - l + 1
            if windowSize - maxFreq > k:
                map[s[l]] -= 1
                l += 1
            else:
                res = max(res, windowSize)
        return res
            
