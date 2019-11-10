# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"

class Solution:
    def FindLongPalinSubstr(self,s):
        
        dp_list =  [[0 for i in range(len(s))] for j in range(len(s))]

        # print(dp_list)

        max_i = 0
        max_j = 0
        max_lensub = 0

        for i in reversed(range(len(s))):
            # print(i)
            for j in range(i,len(s)):
                if i == j:
                    dp_list[i][j] = 1
                elif j == i+1 and s[i]==s[j]:
                    dp_list[i][j] = 1
                elif s[i]==s[j] and dp_list[i+1][j-1] ==1:
                    dp_list[i][j] =1
                if dp_list[i][j]==1:
                    len_sub = abs(i-j)+1
                    if len_sub > max_lensub:
                        max_i = i
                        max_j = j
                        max_lensub = len_sub
        return s[max_i:max_j+1]


if __name__ == "__main__":
    
    s = 'wqefagqasddddddddddsaasgasasddddddddddsaasddddddddddsadwf'
    solu = Solution()
    print(solu.FindLongPalinSubstr(s))