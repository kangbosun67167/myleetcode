# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
#Input:
# [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: true

class Solution:
    def isValidSudoku(self, board) -> bool:
        big = set()
        for i in range(0,9):
            for j in range(0,9):
                print(big)
                if board[i][j]!='.':
                    cur = board[i][j]
                    if (i,cur) in big or (cur,j) in big or (i//3,j//3,cur) in big:
                        return False
                    big.add((i,cur))
                    big.add((cur,j))
                    big.add((i//3,j//3,cur))
        return True
if __name__ == "__main__":
    board = [
                ["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]
            ]
    print(Solution().isValidSudoku(board))