# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place and use only constant extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # key : to maxmium and minmuim

        len_nums  = len(nums)

        # littlebig = nums[len_nums-1]
        point_ = len_nums-1
        for i in range(len_nums-1,-1,-1):
            if i == len_nums-1:
                continue
            if nums[i] < nums[i+1]:
                # tmp = nums[i+1]
                #  = nums[i]
                point_ = i + 1
                while point_ < len_nums and  nums[point_] > nums[i] :
                    point_ += 1
                point_ = point_ - 1
                nums[i],nums[point_] = nums[point_],nums[i]
                nums[i+1:] = sorted(nums[i+1:])
                # point_ = i
                i = -1
                break
        if i != -1:
            nums[:] = sorted(nums)
        print(nums,i)

if __name__ == "__main__":
    nums = [6,3,4,7,5,5,3]
    Solution().nextPermutation(nums)

