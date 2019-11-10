# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Given nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

# It doesn't matter what you leave beyond the returned length.

class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0

        # min_num = nums[0]
        point = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[point-1]:
                nums[point] = nums[i]
                point += 1
        # if len(nums) == point:
        #     nums.append[point]
        # nums[point] = point
        return point

if __name__ == "__main__":
    nums = [1,1,2,3,3,5,5]
    new_nums = Solution().removeDuplicates(nums)
    print(new_nums)

        