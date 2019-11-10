class Solution:
    def myAtoi(self, s):
        num_list = [str(i) for i in range(0,10)]
        pos_neg = ['+',"-"]
        # num_list.apeend('+')
        # num_list.apeend('-')
        sin = 1
        num_out = 0
        flag = 0
        for item in s:
            print(item)
            if item == " ":
                continue
            if item in pos_neg and flag == 0:
                if item == '-':
                    sin = - sin 
                continue
            if item in num_list:
                num_out = num_out *10 + int(item)
                flag=1
                if num_out * sin < -2**31:
                    return -2**31
                if num_out *sin > 2**31 - 1:
                    return 2**31 -1
            else:
                break
    
        return sin*num_out

if __name__ == "__main__":
    s = '   -+12999999999991234'
    int_s = Solution().myAtoi(s)
    print(int_s)    