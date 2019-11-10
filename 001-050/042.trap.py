# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it is able to trap after raining.

# Example:

# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

class Solution:
    def trap(self, height):
        # next_candi = 0
        def dfs(h_l,pre_sum):
            if len(h_l) < 2:
                return pre_sum
            i = 0
            while h_l[i+1] >= h_l[i]:
                i += 1
                if i+1 >= len(h_l):
                    return pre_sum
            max_h = 0
            inter_h_sum = 0
            point_j = -1
            for j in range(i+1,len(h_l)):
                # print(h_l)
                # print(j,i)
                if h_l[j] >= h_l[i]:
                    pre_sum = pre_sum + (j-i-1) * h_l[i] - inter_h_sum
                    return dfs(h_l[j:],pre_sum)
                if h_l[j] > max_h:
                    max_h = h_l[j]
                    point_j = j
                    sencond_sum = inter_h_sum
                inter_h_sum += h_l[j]
            if point_j != -1:
                pre_sum = pre_sum + (point_j-i-1) * h_l[point_j] - sencond_sum
                return dfs(h_l[point_j:],pre_sum)
            else:
                return pre_sum
        
        return dfs(h_l=height,pre_sum=0)

if __name__ == "__main__":
    height = [0,2,0]#[0,1,0,2,1,0,1,3,2,1,2,1]
    print(Solution().trap(height))
            

