# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
# Return the sum of the three integers. You may assume that each input would have exactly one solution.

# Example:

# Given array nums = [-1, 2, 1, -4], and target = 1.

# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution:
    def threeSumClosest(self, nums, target):
        min_sum = 0
        min_ii = float('inf')
        nums = sorted(nums)
        for ii in range(len(nums)):
            new_target = target - nums[ii]
            left_p = ii + 1
            right_p = len(nums)-1
            
            
            while left_p<right_p:
                nowsum = nums[left_p] + nums[right_p] - new_target

                if nowsum == 0:
                    print([ nums[left_p] , nums[right_p] , nums[ii]])
                    return target
                elif nowsum > 0:
                    if abs(nowsum) < min_ii:
                        min_ii = abs(nowsum)
                        min_sum = nums[left_p] + nums[right_p] + nums[ii]
                        print([ nums[left_p] , nums[right_p] , nums[ii]])
                    right_p -= 1
                else:
                    if abs(nowsum) < min_ii:
                        min_ii = abs(nowsum)
                        min_sum = nums[left_p] + nums[right_p] + nums[ii]
                        print([ nums[left_p] , nums[right_p] , nums[ii]])
                    left_p += 1
        return min_sum

if __name__ == "__main__":
    s =  [1,1,1,0]
    t  = -1
    # start = time.time()
    # solu = 
    print(Solution().threeSumClosest(s,t))
    # print(time.time()-start)