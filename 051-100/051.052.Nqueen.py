class Solution:
    def solveNQueens(self, n: int):
        item = ''
        for _ in range(n):
            item += '.'
        chessboard = [item] * n
        out_ = []
        def dfs(chess_b,step=0):
            if step == n:
                # out_chess_b = [s.replace("0", ".") for s in chess_b]
                out_.append(1)

                return
            for j in range(n):
                if chess_b[step][j] != '0':
                    new_chess_ = chess_b[:]
                    
                    new_chess_[step] = new_chess_[step][:j] + 'Q' + new_chess_[step][j+1:]
                    i = step + 1
                    while i < n:
                        # new_chess_[i][j-]
                        left_j = j - (i - step)
                        right_j = j + (i-step)
                        if left_j >=0:
                            # new_chess_[i][left_j] = '0'#new_chess_[i] = new_chess_[i][:left_j] + '0' + new_chess_[i][left_j+1:]
                            new_chess_[i] = new_chess_[i][:left_j] + '0' + new_chess_[i][left_j+1:]
                        if right_j < n:
                            # new_chess_[i][right_j] = '0'
                            new_chess_[i] = new_chess_[i][:right_j] + '0' + new_chess_[i][right_j+1:]
                        new_chess_[i] = new_chess_[i][:j] + '0' + new_chess_[i][j+1:]
                        i += 1
                    # print(new_chess_)
                    dfs(chess_b=new_chess_,step=step+1)
            
        dfs(chess_b=chessboard,step=0)
        return len(out_)

print(Solution().solveNQueens(5))
# s = '123'
# s[1] = '3'
# print(s)