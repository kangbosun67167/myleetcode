# The count-and-say sequence is the sequence of integers with the first five terms as following:

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221

class Solution:
    def countAndSay(self, n: int) -> str:
        
        now_s = '1'

        for _ in range(n-1):
            now_s = self.convert(now_s)
        return now_s

    
    def convert(self,str_):
        
        now_ = str_[0]
        count = 1
        out_ = ''
        for i in str_[1:]:
            if i == now_:
                count += 1
            else:
                out_ = out_ + str(count) + now_
                now_ = i
                count = 1
        out_ = out_ + str(count) + now_
        return out_

if __name__ == "__main__":
    n= 50
    print(Solution().countAndSay(n))
        
