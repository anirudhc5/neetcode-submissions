class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowl, rowr = 0, len(matrix) - 1
        row_of = 0
        while rowl <= rowr:
            c = (rowl + rowr) // 2
            if matrix[c][0] <= target <= matrix[c][-1]:
                row_of = c
                break
            elif target > matrix[c][-1]:
                rowl = c + 1
            else:
                rowr = c - 1
        
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            c = (l + r) // 2
            if matrix[row_of][c] == target:
                return True
            elif matrix[row_of][c] < target:
                l = c + 1
            else:
                r = c - 1
        return False