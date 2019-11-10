# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]\

class Solution:
    def searchRange(self, nums, target):

        if not nums:
            return [-1,-1]
        # binary 
        left_p = 0
        right_p = len(nums) -1

        

            # right_p = right_p + 1
        
        return self.searchRange_(nums,target,left_p,right_p)
        
    def searchRange_(self,nums,target,left_p,right_p):

        # left_p = 0
        # right_p = len(nums)-1
        # out_list = [-1,-1]

        while left_p<=right_p:
            mid_p = (left_p+right_p) // 2
            # print(mid_p)
            if nums[mid_p] == target:
                # out_list = [mid_p,mid_p]
                print(mid_p,nums[mid_p])
                if mid_p > left_p and nums[mid_p-1] == target:
                    print(nums[left_p:mid_p])
                    out = self.searchRange_(nums,target,left_p,mid_p-1)
                    # print(out)
                    left_t = out[0]
                    # pass
                else:
                    left_t = mid_p
                if mid_p < right_p   and nums[mid_p+1] == target:
                    # print(nums[mid_p:right_p+1])
                    out = self.searchRange_(nums,target,mid_p+1,right_p)
                    # print(out)
                    right_t = out[1]
                else:
                    right_t = mid_p
                # if -1 in [left_t,right_t]:
                #     left_t = max(left_t,right_t)
                #     right_t = left_t
                return [left_t,right_t]    
            elif nums[mid_p] < target:
                left_p = left_p + 1
            else:
                right_p = right_p - 1
        
        return [-1,-1]

if __name__ == "__main__":
    nums = [2,2]
    t = 3
    print(Solution().searchRange(nums,t))


