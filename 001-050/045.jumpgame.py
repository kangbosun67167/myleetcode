class Solution:
    def jump(self, nums):
        
        step_list = []
        def helper(nums_,step=0):
            if len(nums_) == 1:
                # print("!!!!!",step)
                step_list.append(step)
            for i in reversed(range(len(nums_)-1)):
                if nums_[i] >= len(nums_)-1 - i:
                    # print(i)
                    # print(nums,nums_)
                    helper(nums_=nums_[:i+1],step=step+1)
        helper(nums_=nums)
        # print(step_list)
        return min(step_list)
    
    def dp(self,nums):
        
        dp = [0] + [float('inf')] * (len(nums) - 1)
        # print(dp)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] + j >= i and dp[j] + 1 < dp[i]:
                    dp[i] = dp[j] + 1   
                    break    
            # print(dp)
        return dp[-1]

    def mydp(self,nums):
        
        dp = [0] + [-1] * (len(nums) - 1)
        # print(len(nums),len(dp))

        # for i in range(len(nums)):
        i = 0
        start = 1
        end = 0
        # end_last =0
        now_step = 0
        # print(dp)
        for i in range(len(nums)):
            # start = max(i+1,end)
            
            # print(end)
            if dp[i] == -1:
                now_step += 1
                dp[start:end] = [now_step]*(end-start)
                start = end
                # print(dp)
            end = max(end,min(i + nums[i] + 1,len(nums)))
            # dp[start,end] = dp[i] + 1
            # end_last = end - 1
            # for j in range(start,end+1):
            #     if j > len(nums) -1: break
            #     dp[j] = min(dp[i] + 1,  dp[j]) 
            # i += 1
            # print(i)

                
        return dp[-1]

nums = [2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,10,1,1,1,1,1,1]
nums = nums * 100
print(Solution().mydp(nums))