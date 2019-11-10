# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

# Note:

# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like ? or *.
# Example 1:

# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Example 2:

# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:

# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
# Example 4:

# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
# Example 5:

# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '?'}

        if p[0] == '*':
            t_i = 0
            p_i = 1
            bool_list = []
            while t_i < len(s) and p_i < len(p):
                if p[p_i] in [s[t_i],'?']:
                    bool_list.append(self.isMatch(s=s[t_i+1:],p=p[2:]))
                t_i += 1
            if not bool_list:
                if t_i == 0:
                    return True
                else:
                    return False
            return any(bool_list)

        elif len(p) > 2 and p[1] == '*':
            t_i = 1
            p_i = 2
            bool_list = []
            while t_i < len(s) and p_i < len(p):
                if p[p_i] in [s[t_i],'?']:
                    bool_list.append(self.isMatch(s=s[t_i+1:],p=p[3:]))
                t_i += 1
            return first_match and any(bool_list)
        else:
            return first_match and self.isMatch(s=s[1:],p=p[1:])

        
    def isMatch_regular(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch_regular(text, pattern[2:]) or
                    first_match and self.isMatch_regular(text[1:], pattern))
        else:
            return first_match and self.isMatch_regular(text[1:], pattern[1:])              
    
    def isMatch_dp(self, s, p):
        l = len(s)
        if len(p) - p.count('*') > l:
            return False
        dp = [True]  + [False] * l
        for letter in p:
            new_dp = [dp[0] and letter == '*']
            if letter == '*':
                for j in range(l):
                    new_dp.append(new_dp[-1] or dp[j + 1])
            elif letter == '?':
                new_dp += dp[:l]
            else:
                new_dp += [dp[j] and s[j] == letter for j in range(l)]
            dp = new_dp
            print(dp)
        return dp[-1]
        
if __name__ == "__main__":
    
    t = "leetcode"

    p = "*e*t?od*"
    print(Solution().isMatch_dp(t,p))