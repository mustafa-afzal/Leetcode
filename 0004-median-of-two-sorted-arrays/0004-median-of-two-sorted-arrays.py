class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        for i in range(len(nums1)):
            res.append(nums1[i])
        for i in range(len(nums2)):
            res.append(nums2[i])
        res = sorted(res)
        if len(res) % 2 == 0:
            num1 = len(res) // 2
            num2 = num1 - 1
            return (res[num1] + res[num2]) / 2
        else:
            num1 = len(res) // 2
            return res[num1]