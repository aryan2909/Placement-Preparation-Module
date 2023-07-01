class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        if m * n != r * c:
            return mat
        
        reshaped = [[0] * c for _ in range(r)]
        row = 0
        col = 0
        
        for i in range(m):
            for j in range(n):
                reshaped[row][col] = mat[i][j]
                col += 1
                
                if col == c:
                    row += 1
                    col = 0
        
        return reshaped
