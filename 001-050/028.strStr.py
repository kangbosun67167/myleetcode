# Implement strStr().

# Return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:

# What should we return when needle is an empty string? 
# This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. 
# This is consistent to C's strstr() and Java's indexOf().

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack:
            if not needle:
                return 0
            return -1
        len_needle = len(needle)
        for i in range(len(haystack)):
            if i + len_needle > len(haystack):
                break
            if haystack[i:i+len_needle] == needle:
                return i
        return -1

if __name__ == "__main__":
    
    haystack = ""

    needle = "a"
    print(Solution().strStr(haystack,needle))
        