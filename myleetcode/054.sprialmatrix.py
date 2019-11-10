class Solution:
    def spiralOrder(self, matrix):
        out_ = []

        def digui(matrix_):
            if not matrix_:
                return
            mat_i_len = len(matrix_)
            mat_j_len = len(matrix_[0])
            if mat_j_len == 0:
                return
            if mat_i_len == 1:
                # print(matrix_)
                out_.extend(matrix_[0])
                return
            if mat_j_len == 1:
                out_.extend([matrix_[i][0] for i in range(mat_i_len)])
                return
            for i in range(mat_i_len):
                if i==0:
                    out_.extend(matrix_[0])
                elif i < mat_i_len -1 :
                    out_.append(matrix_[i][-1])

            for j in reversed(range(mat_i_len)):
                if j == mat_i_len -1:
                    out_.extend([matrix_[j][i] for i in reversed(range(mat_j_len))])
                elif j > 0:
                    out_.append(matrix_[j][0])
            next_mat = [[matrix_[i][j] for j in range(1,mat_j_len-1)] for i in range(1,mat_i_len-1)]
            print(out_)
            print(next_mat)
            digui(matrix_=next_mat)
        
        digui(matrix)
        return out_

mat = [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]

print(Solution().spiralOrder(mat))