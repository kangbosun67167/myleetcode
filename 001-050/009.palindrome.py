class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        num_list = []
        div_x = x
        while True:
            yu_x = div_x%10
            div_x = div_x//10
            # print(yu_x)
            num_list.append(yu_x)
            if div_x == 0:
                break
        
        # divsor = 1
        multi = 0
        for i in range(len(num_list)//2+1):
            # print(num)
            multi = multi * 10 + num_list[i]
        # a =1
        divsor = 10 ** (len(num_list)//2)
        if len(num_list)%2 == 0:
            divsor = divsor // 10 
        # print(multi, x //divsor)
        if multi == x // divsor:
            return True
        
        return False

if __name__ == "__main__":
    
    x = 11100011111100011111
    print(Solution().isPalindrome(x))