class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            if not self.isUnique(row):
                return False
        

        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self.isUnique(column):
                return False
        

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [board[row][col] for row in range(i, i+3) for col in range(j, j+3)]
                if not self.isUnique(sub_box):
                    return False
        
        return True
    
    def isUnique(self, arr: List[str]) -> bool:
        seen = set()
        for elem in arr:
            if elem != '.':
                if elem in seen:
                    return False
                seen.add(elem)
        return True
