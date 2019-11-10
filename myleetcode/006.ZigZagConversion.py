# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
#  (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:

# P     I    N
# A   L S  I G
# Y A   H R
# P     I

class Solution:
    def zigzag(self,s,row):
        new_s = ''
        len_s = len(s)
        # row =len_s/
        if row ==1:
            return s
        for i in range(row):
            if i ==0 or i == row-1:
                # new_s.append()
                j = i
                while j <len_s:
                    new_s += s[j]
                    j += (row-1)*2
            else:
                j = i 
                
                while j <len_s:
                    new_s += s[j]
                    j += (row-i-1)*2
                    if j <len_s:
                        new_s += s[j]
                        j += 2*i




        return str(new_s)


if __name__ == "__main__":
    
    s = "PAYPALISHIRING"
    solu = Solution()
    print(solu.zigzag(s,3))