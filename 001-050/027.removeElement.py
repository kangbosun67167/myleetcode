# Given an array nums and a value val, remove all instances of that value in-place 
# and return the new length.

# Do not allocate extra space for another array, 
# you must do this by modifying the input array in-place with O(1) extra memory.

# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# Example 1:

# Given nums = [3,2,2,3], val = 3,

# Your function should return length = 2, with the first two elements of nums being 2.

# It doesn't matter what you leave beyond the returned length

class Solution:
    def removeElement(self, nums, val) -> int:

        if not nums:
            return 0
        if val not in nums:
            return len(nums)

        nums = sorted(nums)
        point = 0
        i = 0
        for i in range(len(nums)):
            if nums[i] == val and point == i:
                point = i + 1
                while point < len(nums) and nums[point] == nums[i]:
                    point += 1
            
            if point >= len(nums):
                # print(point)
                break
            nums[i] = nums[point]
            # print(i, point)
            point = point + 1
        return i,nums[:i]
    def nosorted(self,nums,val):


        if not nums:
            return 0
        if val not in nums:
            return len(nums)
        point = 0
        

        for i in range(len(nums)):
            # print(i,point)
            if point >= len(nums):
                break
            if nums[point] == val:
                while point < len(nums) and nums[point] == val:
                    point += 1
                # print(point)
            if point >= len(nums):
                break

            
            nums[i] = nums[point]
            # print(i,point,nums[i])
            point = point + 1

        return i

if __name__ == "__main__":
    nums = [4,5]
    new_nums = Solution().nosorted(nums,4)
    print(new_nums)

