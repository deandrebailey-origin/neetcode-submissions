class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix)-1
        m = 0

        while start <= end:
            mid = (start + end) // 2
            if target < matrix[mid][0]:
                end = mid - 1
            elif target > matrix[mid][-1]:
                start = mid + 1
            else:
                m = mid
                break
        
        l, r = 0, len(matrix[m]) - 1
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[m][mid]:
                r = mid - 1
            elif target > matrix[m][mid]:
                l = mid + 1
            else:
                return True
        
        return False


