# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution:
    def generateParenthesis(self, n):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans
    
    def mybacktracking(self,n):
        out_ = list()
        def backtracking(s='',left=0,right=0):
            if len(s) == 2*n:
                out_.append(s)
                return 
            if left < n:
                backtracking(s+'(',left+1,right)
            if right < left :
                backtracking(s+')',left,right+1)
        backtracking()
        return out_


if __name__ == "__main__":
    print(Solution().mybacktracking(3))


                