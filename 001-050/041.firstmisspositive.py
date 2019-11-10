# Given an unsorted integer array, find the smallest missing positive integer.

# Example 1:

# Input: [1,2,0]
# Output: 3
# Example 2:

# Input: [3,4,-1,1]
# Output: 2
# Example 3:

# Input: [7,8,9,11,12]
# Output: 1
# Note:

# Your algorithm should run in O(n) time and uses constant extra space.

class Solution:
    def firstMissingPositive(self, nums) -> int:
        nums.sort()
        now = 1
        for i in range(len(nums)):
            # if nums[i] <= 0 :
                # continue
            # if nums[i] == now -1:
                # continue
            if nums[i] == now:
                # return now
                now  += 1
        return now
    def newfinder(self,nums):
        
        new_nums = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] <=0 or nums[i] > len(nums):
                continue
            new_nums[nums[i] - 1] = nums[i]
        # print(new_nums)

        for ii in range(len(new_nums)):
            if new_nums[ii] != ii+1:
                return ii+1
            if ii == len(new_nums)-1:
                return new_nums[ii] + 1 
        return 1
        # pass
    def O1_finder(self,nums):
        for i in range(len(nums)):
            # if nums[i] <= 0 or nums[i] > len(nums):
            #     continue
            while 0 < nums[i] <= len(nums) and nums[nums[i] -1] != nums[i]:
                tmp = nums[i] -1
                nums[tmp],nums[i] = nums[i],nums[tmp]
            # print(nums)
        now = 1
        for i in range(len(nums)):
            # if nums[i] <= 0 :
                # continue
            # if nums[i] == now -1:
                # continue
            if nums[i] == now:
                # return now
                now  += 1
        return now
if __name__ == "__main__":
    
    nums =[1,1]
    print(Solution().O1_finder(nums))
        