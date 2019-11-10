# ```
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true
# ```


class Solution:
    def IsValid(self,s):
        stack = []
        left_sym = ['(','[','{']
        right_sym = [')',']','}']

        for item in s:
            if item in right_sym:
                if len(stack) == 0:
                    return False
                pop_item =  stack.pop()
                if pop_item in left_sym:
                    if left_sym.index(pop_item) == right_sym.index(item):
                        continue
                    else:
                        return False
            stack.append(item)
        if len(stack) == 0:
            return True
        return False

if __name__ == "__main__":
    
    s = '[{'
    solu = Solution()
    print(solu.IsValid(s))