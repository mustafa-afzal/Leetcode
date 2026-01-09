class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in dict1:
                return [dict1[diff], i]
            else:
                dict1[v] = i
        
            
            

        


                