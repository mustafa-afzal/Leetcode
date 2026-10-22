class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        maxLen = 0
        for r in range(l, len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            w = (r - l) + 1
            maxLen = max(w, maxLen)
            charSet.add(s[r])
        return maxLen