from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       dictNums = Counter(nums)
       max_key = max(dictNums, key=dictNums.get)
       return max_key
            