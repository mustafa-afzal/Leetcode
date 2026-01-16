class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, maxCount = 0, 0
        best = 0
        freq = {}
        for r in range(len(s)):
            length = (r - l) + 1
            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1
            maxCount = max(maxCount, freq[s[r]])
            while length - maxCount > k:
                freq[s[l]] -= 1
                l += 1
                length = (r - l) + 1
            best = max(best, length)
        return best

