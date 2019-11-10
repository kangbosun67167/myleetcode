# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
import time 
class Solution:
    def FinaAll3Sum0(self,num_list):
        
        all_list = list()
        neg_num_list = []
        pos_num_list = []
        cnt_0 = 0
        for i in range(len(num_list)):
            if num_list[i]<0:
                neg_num_list.append(num_list[i])
            else:
                if num_list[i] == 0:
                    cnt_0 += 1
                pos_num_list.append(num_list[i])
        if cnt_0 >= 3:
            all_list.append([0,0,0])
        
        for neg_num in neg_num_list:
            for i in range(len(pos_num_list)):
                for j in range(i+1,len(pos_num_list)):
                    if pos_num_list[i] + pos_num_list[j] == - neg_num:
                        solve_list = sorted([neg_num,pos_num_list[i],pos_num_list[j]])
                        if solve_list not in all_list:
                            print(solve_list)
                            all_list.append(solve_list)
        for pos_num in pos_num_list:
            for i in range(len(neg_num_list)):
                for j in range(i+1,len(neg_num_list)):
                    if neg_num_list[i] + neg_num_list[j] == - pos_num:
                        solve_list = sorted([pos_num,neg_num_list[i],neg_num_list[j]])
                        if solve_list not in all_list:
                            print(solve_list)
                            all_list.append(solve_list)
        
        
        return all_list

    def Find3Sum(self,num_list):
        num_list = sorted(num_list)
        all_list = list()
        len_num = len(num_list)
        # cnt =0
        pre_target = float('-inf')
        for sum_point in range(len_num):
            
            left_point = sum_point+1
            right_point = len_num-1


            sum_target = num_list[sum_point]
            if sum_target == pre_target:
                continue
            
            # fore_right = left_point
            # hind_right = right_point

            while left_point<right_point:
                if left_point == sum_point:
                    left_point +=1
                    continue
                if right_point == sum_point:
                    right_point -=1
                    continue
                if num_list[left_point] + num_list[right_point] == - sum_target:
                    solve_list = [sum_target,num_list[left_point],num_list[right_point]]
                    # if solve_list not in all_list:
                    # if solve_list in all_list:
                    #     print(solve_list)
                    #     cnt +=1
                    # print(sum_point,left_point,right_point)
                    all_list.append(solve_list)


                    if left_point < len_num-1:
                        # print(left_point,'!')
                        while num_list[left_point+1] == num_list[left_point]:
                            left_point  += 1
                            if left_point+1 >=len_num:
                                break
                    if right_point > 0:
                        while num_list[right_point-1] == num_list[right_point]:
                            right_point -= 1
                            if right_point -1 < 0:
                                break
                    
                    right_point -= 1
                    left_point  += 1
                    # continue
                elif num_list[left_point] + num_list[right_point] > - sum_target:
                    right_point -= 1
                    # right_point = int((right_point+left_point)/2)
                else:
                    left_point +=1
            pre_target = sum_target
        return all_list

    def Find3Sum_binary(self,num_list):
        num_list = sorted(num_list)
        all_list = list()


        for sum_point in range(len(num_list)):
            
            left_point = sum_point+1
            right_point = len(num_list)-1


            # mid_point = int((ho+hi)/2)

            sum_target = num_list[sum_point]

            # fore_right = left_point
            # hind_right = right_point
            for left_point in range(sum_point+1,len(num_list)-1):
                if num_list[left_point]>=0:
                        break
                ho = left_point + 1
                hi = len(num_list)-1
                # print(left_point)
                while ho<=hi:
                    mid_point = int((ho+hi)/2)
                    if num_list[left_point] + num_list[mid_point] == - sum_target:
                        solve_list = sorted([sum_target,num_list[left_point],num_list[mid_point]])
                        if solve_list not in all_list:
                            all_list.append(solve_list)
                            # print(solve_list)
                        break
                    elif num_list[left_point] + num_list[mid_point] > - sum_target:
                        hi = mid_point -1
                        # right_point = int((right_point+left_point)/2)
                    else:
                        ho = mid_point + 1
                    
        return all_list


if __name__ == "__main__":
    s = [0,0,0]
    # start = time.time()
    solu = Solution()
    print(solu.Find3Sum(s))
    # print(time.time()-start)