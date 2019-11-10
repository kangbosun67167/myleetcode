# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

class Solution:
    def search(self, nums, target) -> int:
        # binary 

        left_p = 0
        right_p = len(nums)-1

        while left_p <= right_p:
            now_p = int(left_p + right_p) // 2
            print(nums[now_p])

            if nums[now_p] == target:
                return now_p
            elif nums[now_p] > target:
                # if now_p == 0:
                #     break
                if nums[left_p] <= nums[now_p] and target >= nums[left_p]:
                    right_p = now_p - 1
                elif nums[left_p] > nums[now_p]:
                    right_p = now_p - 1
                else:
                    left_p = now_p + 1
            else:
                # if now_p == len(nums)-1:
                #     break
                if nums[now_p] <= nums[right_p] and target <= nums[right_p]:
                    left_p = now_p + 1
                elif nums[now_p] > nums[right_p]:
                    left_p = now_p + 1
                else:
                    right_p = now_p - 1
                
        return -1
if  __name__ == "__main__":
    nums = [3,1]
    target = 1
    print(Solution().search(nums,target))