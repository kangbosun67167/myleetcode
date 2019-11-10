# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

class Solution:
    def maxSubArray(self, nums):
        dp = [nums[0]] + [0] * (len(nums)-1)
        for i in range(1,len(nums)):
            if dp[i-1] <=0:
                dp[i] = nums[i]
            else:
                dp[i] = nums[i] + dp[i-1]
        # print(dp)
        return max(dp)

print(Solution().maxSubArray(nums=[-2,1,-3,4,-1,2,4,5,6,32,2,1,-5,4]))