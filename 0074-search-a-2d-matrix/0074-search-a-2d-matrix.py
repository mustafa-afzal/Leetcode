class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1
        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break
        if not (top <= bot):
            return False
        l, r = 0, COLS - 1
        while l <= r:
            midCol = (l + r) // 2
            if target > matrix[mid][midCol]:
                l = midCol + 1
            elif target < matrix[mid][midCol]:
                r = midCol - 1
            else:
                return True
        return False