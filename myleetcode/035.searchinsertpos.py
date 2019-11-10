# Given a sorted array and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Example 1:

# Input: [1,3,5,6], 5
# Output: 2
# Example 2:

# Input: [1,3,5,6], 2
# Output: 1
# Example 3:

# Input: [1,3,5,6], 7
# Output: 4
# Example 4:

# Input: [1,3,5,6], 0
# Output: 0

class Solution:
    def searchInsert(self, nums, target: int) -> int:
        left_p = 0
        right_p= len(nums) - 1

        while left_p <= right_p:
            mid_p = (left_p+right_p) // 2
            # print(left_p,right_p,mid_p)
            if nums[mid_p] == target:
                return mid_p
            elif nums[mid_p] < target:
                left_p += 1
            else:
                right_p -= 1
        
        return min(left_p,right_p) + 1
if __name__ == "__main__":

    nums = [0,1,2,4,5,6]
    t = -1
    print(Solution().searchInsert(nums,t))    