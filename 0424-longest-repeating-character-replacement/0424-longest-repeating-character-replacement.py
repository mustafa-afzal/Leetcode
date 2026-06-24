class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = {}
        maxWindow = 0
        l = 0
        for r in range(len(s)):
            map[s[r]] = map.get(s[r], 0) + 1
            windowSize = r - l + 1
            maxFreq = max(map.values())
            if windowSize - maxFreq > k:
                map[s[l]] -= 1
                if map[s[l]] == 0:
                    del map[s[l]]
                l += 1
            maxWindow = max(r - l + 1, maxWindow)
        return maxWindow