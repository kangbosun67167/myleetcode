# Given a collection of candidate numbers (candidates) and a target number (target), 
# find all unique combinations in candidates where the candidate numbers sums to target.

# Each number in candidates may only be used once in the combination.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
class Solution:
    def combinationSum_(self, candidates, target):
            candidates.sort()
            out_list = []
            def dfs(target,index,list_to_save):

                if target < 0:
                    return
                if target ==0:
                    if list_to_save not in out_list:
                        out_list.append(list_to_save)
                    return
                for i in range(index,len(candidates)):
                    dfs(target - candidates[i],index=i+1,list_to_save = list_to_save + [candidates[i]])
            dfs(target,index=0,list_to_save=[])
            return out_list
    

if __name__ == "__main__":
    candi = [5,2,1,2,3,3]
    t = 8
    out_list = Solution().combinationSum_(candi,t)
    for item in out_list:
        print(item)