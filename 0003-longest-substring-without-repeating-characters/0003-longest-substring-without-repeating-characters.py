class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            w = (r - l) + 1
            longest = max(w, longest)
            charSet.add(s[r])
        return longest
        
                
                
                    

