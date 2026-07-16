class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset, colset, boxset = set(), set(), set()
        for i in range(9):
            rowset=set()
            for j in range(9):
                if board[i][j]==".":
                    continue
                elif board[i][j] in rowset:
                    return False
                else:
                    rowset.add(board[i][j])
            
        for k in range(9):
            colset=set()
            for l in range(9):
                if board[l][k]==".":
                    continue
                elif board[l][k] in colset:
                    return False
                else:
                    colset.add(board[l][k])
        for box_row in range(0, 9, 3):     
            for box_col in range(0, 9, 3): 
        
                boxset = set() 
        
                for r in range(3):         
                    for c in range(3):     
                
                        val = board[box_row + r][box_col + c]
                
                        if val == ".":
                            continue
                        if val in boxset:
                            return False
                        boxset.add(val)

        else:
            return True


