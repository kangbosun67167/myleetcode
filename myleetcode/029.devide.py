# Given two integers dividend and divisor, divide two integers without using multiplication, 
# division and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero.

# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Example 2:

# Input: dividend = 7, divisor = -3
# Output: -2
# Note:

# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers 
# within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, 
# assume that your function returns 231 − 1 when the division result overflows.

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        pos_ = 1
        if dividend*divisor < 0:
            pos_ = -1
        dividend,divisor = abs(dividend),abs(divisor)

        str_end = str(dividend)
        # str_sor = str(divisor)
        print(str_end,divisor)

        i = 0
        now_end = 0
        out_list = 0
        while i < len(str_end):
            now_end = now_end * 10 + int(str_end[i])
            out_ = 0
            while divisor <= now_end:
                now_end = now_end - divisor
                out_ = out_ + 1
            out_list = out_list * 10 + out_
            i += 1
        if out_list*pos_ < - 2**31:
            return - 2**31
        if out_list*pos_ > 2 ** 31 -1:
            return 2**31 -1
        return out_list*pos_


if __name__ == "__main__":
    end = 100
    div = -1
    print(Solution().divide(end,div))