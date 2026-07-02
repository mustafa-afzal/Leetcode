class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l, r = 0, (rows * cols - 1)
        while l <= r:
            mid = (l + r) // 2
            rowMid = mid // cols
            colMid = mid % cols
            if target < matrix[rowMid][colMid]:
                r = mid - 1
            elif target > matrix[rowMid][colMid]:
                l = mid + 1
            else:
                return True
        return False
