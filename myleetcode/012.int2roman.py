# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

# Example 1:

# Input: 3
# Output: "III"
# Example 2:

# Input: 4
# Output: "IV"
# Example 3:

# Input: 9
# Output: "IX"
# Example 4:

# Input: 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
# Example 5:

# Input: 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

class Solution:
    def intToRoman(self, num: int) -> str:

        mutli = 1
        roman_ = []
        while num!=0:
            delta = num%10

            # print(delta,mutli)
            roman_.append(self.convert(delta,mutli))
    
            mutli *= 10
            num = num // 10

        roman_s  = ''
        for item in reversed(roman_):
            # print(item)
            if item != '':
                roman_s += item
        return roman_s
    def convert(self,num,mutli):
        if num*mutli > 1000:
            M_num = num*mutli // 1000
            roman_s  = ''
            for _ in range(M_num):
                roman_s += 'M'
            return roman_s
        if num == 0:
            return ''
        
        list_roman = ['I','V','X','L','C','D','M']
        list_int = [1,5,10,50,100,500,1000]

        for i in range(len(list_int)):
            if num*mutli > list_int[i]:
                continue
            if num*mutli == list_int[i]:
                 return list_roman[i]
            elif num >1 and num <5:
                if  num == 4:
                    return list_roman[i-1] + list_roman[i]
                else:
                    out_romen = ''
                    for _ in range((num*mutli) // list_int[i-1]):
                        out_romen += list_roman[i-1]
                    return out_romen
            elif num > 5 and num <10:
                if  num == 9:
                    return list_roman[i-2] + list_roman[i]
                else:
                    out_romen = list_roman[i-1]
                    for _ in range((num*mutli - list_int[i-1]) // list_int[i-2]):
                        out_romen += list_roman[i-2]
                    return out_romen
            else:
                return ValueError
                    
        # return roman_s
        # return 'T'
if __name__ == "__main__":
    
    a = 1008
    print(Solution().intToRoman(a))