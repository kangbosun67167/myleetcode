# Given an array nums of n integers and an integer target, are there elements a, b, c, 
# and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note:

# The solution set must not contain duplicate quadruplets.

class Solution:
    def fourSum(self, nums, target):
        
        nums = sorted(nums)
        solve_list = []
        for first_num_p in range(len(nums)):
            if first_num_p > 0 and nums[first_num_p] == nums[first_num_p-1]:
                    continue
            for second_num_p in range(first_num_p+1,len(nums)):
                if second_num_p > first_num_p+1 and nums[second_num_p] == nums[second_num_p-1]:
                    continue
                new_target = target - nums[first_num_p] - nums[second_num_p]
                left_p = second_num_p + 1
                right_p = len(nums) - 1
                while left_p<right_p:
                    if nums[left_p] + nums[right_p] == new_target:
                        # print([first_num_p,second_num_p,left_p,right_p])
                        solve_list.append([nums[first_num_p],nums[second_num_p],nums[left_p],nums[right_p]])

                        # print(left_point,'!')
                        while left_p < len(nums)-1 and nums[left_p+1] == nums[left_p]:
                            left_p  += 1


                        while  right_p > 0 and nums[right_p-1] == nums[right_p]:
                            right_p -= 1
                  
                        left_p = left_p + 1
                        right_p = right_p -1
                    elif nums[left_p] + nums[right_p] < new_target:
                        left_p = left_p + 1
                    else:
                        right_p = right_p -1
        return solve_list

if __name__ == "__main__":

    

    num_s = [-1,-5,-5,-3,2,5,0,4]
    target = -7
    print(Solution().fourSum(num_s,target))
        