class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowCheck = [set() for i in range(9)]
        colCheck = [set() for i in range(9)]
        boxCheck = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch == ".": continue
                boxidx = (j//3) + 3*(i//3)
                print(i, j, boxidx)
                print(colCheck)
                if ch in boxCheck[boxidx]: 
                    print("failed box check")
                    return False
                if ch in rowCheck[i]: 
                    print("failed row check")
                    return False
                if ch in colCheck[j]: 
                    print("failed col check")
                    return False
                boxCheck[boxidx].add(ch)
                rowCheck[i].add(ch)
                colCheck[j].add(ch)
        
        return True



        