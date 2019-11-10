# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Note:

# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.

class Solution:
    def Issymequ(self,base_c,c):
        if base_c == '.' or base_c == c:
            return True
        return False

    def isMatch(self, s: str, p: str) -> bool:
        # 递归方式
        point_s = 0
        point_p = 0

        if not p:
            return not s



        while True:

            now_s = s[point_s]
            now_p = p[point_p]
            if self.Issymequ(now_p,now_s):
                if point_s == len(s) - 1 and point_p == len(p) -1:
                    return True
                # point_s += 1
                point_p += 1
                if point_p < len(p) and p[point_p] == '*':
                    while self.Issymequ(p[point_p-1],s[point_s]):
                            if point_s == len(s) - 1:
                                if point_p == len(p) -1:
                                    return True
                                else:
                                    return self.isMatch(s[point_s:],p[point_p+1:])
                            point_s = point_s+1
                    point_p += 1
                else:
                    point_s +=1
                self.isMatch(s[point_s:],p[point_p:])


            else:
                if point_s == len(s) - 1 and point_p == len(p) -1:
                    return False

                point_p = point_p+1
                if point_p < len(p) and p[point_p] == '*':
                    point_p = point_p+1
                    point_s = point_s+1
                    self.isMatch(s[point_s:],p[point_p:])
                else:
                    return False

    # class Solution(object):
    def isMatch_tea(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch_tea(text, pattern[2:]) or
                    first_match and self.isMatch_tea(text[1:], pattern))
        else:
            return first_match and self.isMatch_tea(text[1:], pattern[1:])              
               


if __name__ == "__main__":

    p = 'a.c.e*d*dde*f*'
    s = 'abccddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'

    print(Solution().isMatch_tea(s,p))


