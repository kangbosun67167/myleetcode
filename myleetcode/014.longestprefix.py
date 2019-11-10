# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.

class Solution:
    def findlongestprestr(self,strs):
        
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        
        str0 = strs[0]
        min_len = float('inf')
        for i in range(1,len(strs)):
            len_i = 0
            for j in range(min(len(str0),len(strs[i]))):
                if str0[j] == strs[i][j]:
                    len_i +=1
                else:
                    break
            # print(len_i)
            if len_i < min_len:
                min_len = len_i
        # print(max_len)
        return str0[:min_len]


if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    print(Solution().findlongestprestr(strs))