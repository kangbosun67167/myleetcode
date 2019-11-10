# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# Example 1:

# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:

# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"

class Solution:
    def longestValidParentheses(self, s):



        # count = 0
        if not s:
            return 0
        len_s = len(s)
        i = 0
        while i < len_s and s[i] == ')':
            # if :
            i += 1
        end = len_s
        while end > i  and not self.IsPar(s[i:end]):
            end -= 1
        count = end - i
        if end == 0:
            end = 1
        # print(count,s[end:])
        return max(count,self.longestValidParentheses(s[end:]))


    def IsPar(self,s):
        if s[0] == ')':
            return False
        list_items = []
        for i in range(len(s)):
            if s[i] == ')' and len(list_items) > 0:
                if list_items[-1] == '(':
                    list_items.pop()
            else:
                list_items.append(s[i])
        return not list_items


    def longestValidParentheses_dp(self, s):
        dp, stack = [0]*(len(s) + 1), []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    p = stack.pop()
                    
                    dp[i + 1] = dp[p] + i - p + 1
                    print(p,i, dp[p] + i - p + 1,dp)
        return max(dp)
    
    def mylongestvp(self,s):
        dp = [0]*(len(s)+1)
        max_len = 0
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            if len(stack) > 0 and s[i] == ')':
                stack.pop()
                dp[i+1] = dp[i] + 2
                dp[i+1] = dp[i+1] + dp[i+1-dp[i+1]]
                if dp[i+1] > max_len:
                    max_len = dp[i+1]
        return max_len
if __name__ == "__main__":
    s = "()"
    print(Solution().longestValidParentheses_dp(s))
    print(Solution().mylongestvp(s))
