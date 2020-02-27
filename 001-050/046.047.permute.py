# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


class Solution:
    def permute(self, nums):
        out_ = []
        def digui(saved_,nums_):
            if len(nums_) == 0:
                out_.append(saved_)
                return
            # print(saved_)
            for i in range(len(nums_)):
                # print(saved_,[nums_[i]])
                digui(saved_=saved_ +[nums_[i]],nums_=nums_[:i]+nums_[i+1:])
        digui(saved_=[],nums_=nums)
        return out_

    def permuteUnique(self, nums):
        out_ = []
        def digui(saved_,nums_):
            if len(nums_) == 0:
                if saved_ not in out_:  out_.append(saved_)
                return
            # print(saved_)
            for i in range(len(nums_)):
                # print(saved_,[nums_[i]])
                digui(saved_=saved_ +[nums_[i]],nums_=nums_[:i]+nums_[i+1:])
        digui(saved_=[],nums_=nums)
        return out_
    
    def permuteUnique_fast(self, nums):
        if len(nums) < 2:
            return [nums]
        
        ans, used = [], {}
        
        for i in range(len(nums)):
            if nums[i] not in used:
                suffixes = self.permuteUnique_fast(nums[:i] + nums[i + 1:])
                for suffix in suffixes:
                    ans.append([nums[i]] + suffix)
                
                used[nums[i]] = 1
        return ans

if __name__ == "__main__":
    nums = [1,1,2]
    print(Solution().permuteUnique_fast(nums))