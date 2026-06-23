class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        l = 0
        maxLen = 0
        for r in range(l, len(s)):
            while s[r] in map and l < r:
                map[s[l]] -= 1
                if map[s[l]] == 0:
                    del map[s[l]]
                l += 1
            map[s[r]] = map.get(r, 0) + 1
            maxLen = max(r - l + 1, maxLen)
        return maxLen

