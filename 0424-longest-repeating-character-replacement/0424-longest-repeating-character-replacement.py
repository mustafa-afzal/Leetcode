class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        maxLen = 0
        for r in range(l, len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxFreq = max(freq.values())
            while l < len(s) and (r - l + 1) - maxFreq > k:
                freq[s[l]] = freq.get(s[l], 0) - 1
                l += 1
            maxLen = max(r - l + 1, maxLen)
        return maxLen