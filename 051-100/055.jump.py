class Solution:
    def canJump(self, nums):
        if nums[0] == 0 and len(nums) != 1:
            return False

        dp = [False] * len(nums)
        dp[0]  = True

        end = 0

        for i in range(len(nums)):
            if not dp[i]:
                if end >= i:
                    dp[i:end+1] = [True] * (end+1-i)
                    # end = max(end,min(i+nums[i],len(nums)-1))
            if dp[i]:
                end = max(end,min(i+nums[i],len(nums)-1))
            # print(end)
            print(dp)
        return dp[-1]

nums = [2,3,1,1,2,0,1,4]
Solution().canJump(nums)



