# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# Empty cells are indicated by the character '.'.

class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        stack1 = [(i, j) for i in range(9) for j in range(9) if board[i][j] == "."]
        stack2 = []
        
        def dfs(board):
            if not stack1: return
            x, y = stack1.pop()
            stack2.append((x, y))
            box = [board[x//3*3+i][y//3*3+j] for i in range(3) for j in range(3)]
            row = [board[x][j] for j in range(9)]
            col = [board[i][y] for i in range(9)]
            for i in "123456789":
                # print(i)
                if not any([i in box, i in col, i in row]):
                    board[x][y] = i
                    dfs(board)
                    if not stack1: return
            board[x][y] = "."
            pos = stack2.pop()
            # print(pos,x,y)
            stack1.append(pos)
            # print("!!!")
            # return False
        dfs(board)
    
    def isValidSudoku(self, board) -> bool:
        big = set()
        for i in range(0,9):
            for j in range(0,9):
                # print(big)
                if board[i][j]!='.':
                    cur = board[i][j]
                    if (i,cur) in big or (cur,j) in big or (i//3,j//3,cur) in big:
                        return False
                    big.add((i,cur))
                    big.add((cur,j))
                    big.add((i//3,j//3,cur))
        return True

    def mysolver(self,board):

        # if not self.isValidSudoku(board):
        #     return

        stack_un = [(i,j) for i in range(9) for j in range(9) if board[i][j] == '.']
        stack_do = []
        

        def digui(board):
            if not stack_un: 
                return
            x,y = stack_un.pop()
            stack_do.append((x,y))

            box = [board[x//3*3+i][y//3*3+j] for i in range(3) for j in range(3)]
            row = [board[x][j] for j in range(9)]
            col = [board[i][y] for i in range(9)]
            # print(x,y)
            # print(board[7][:])
            # print(board[1][8])
            # print(board[x//3 *3 : x//3*3 +3][y//3*3:y//3*3+3])
            # print(row,col,box)

            # return
            
            for i in '123456789':
                # 
                if any([i in row,i in col,i in box]):
                    # board[x][y] = '.'
                    continue
                board[x][y] = i
                digui(board)
                if not stack_un:
                    return
            board[x][y] = '.'
            stack_do.pop()
            stack_un.append((x,y))
        digui(board)

   

if __name__ == "__main__":

    board =[[".",".",".","2",".",".",".","6","3"],
            ["3",".",".",".",".","5","4",".","1"],
            [".",".","1",".",".","3","9","8","."],
            [".",".",".",".",".",".",".","9","."],
            [".",".",".","5","3","8",".",".","."],
            [".","3",".",".",".",".",".",".","."],
            [".","2","6","3",".",".","5",".","."],
            ["5",".","3","7",".",".",".",".","8"],
            ["4","7",".",".",".","1",".",".","."]]
    Solution().mysolver(board)
    print(board)
        