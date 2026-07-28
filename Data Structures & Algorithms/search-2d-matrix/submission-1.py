class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows=len(matrix)
        cols= len(matrix[0])
        for i in range(rows):
            if matrix[i][0]<=target and matrix[i][cols-1]>=target:
                low, high = 0, cols-1
                while low<=high:
                    mid = (high+low)//2

                    if matrix[i][mid]==target:
                        return True
                    elif matrix[i][mid]> target:
                        high = mid-1
                    else:
                        low =mid+1
        return False