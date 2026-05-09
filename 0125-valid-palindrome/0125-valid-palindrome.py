class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        sLower = s.lower()
        while l < r:
            if sLower[l].isalnum() and sLower[r].isalnum() and sLower[l] == sLower[r]:
                l += 1
                r -= 1
            elif not sLower[l].isalnum():
                l += 1
            elif not sLower[r].isalnum():
                r -= 1
            else:
                return False
        return True