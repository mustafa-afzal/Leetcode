class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = start + 1
        longest = 0
        sSet = set()
        if s: 
            longest = 1
            sSet.add(s[start])
        while end < len(s):
            length = end - start
            while end < len(s) and s[end] not in sSet:
                length += 1
                sSet.add(s[end])
                end += 1
            if end < len(s):
                sSet.remove(s[start])
                start += 1
            longest = max(length, longest)
        return longest




        
            