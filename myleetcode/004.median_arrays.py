#utf-8!

# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

class Solution:
    def findMedianSortedArrays_force(self, nums1, nums2):
        new_list = []
        i,j=0,0
        while True:
            if len(nums1) == 0:
                new_list = nums2
                break
            if len(nums2) == 0:
                new_list = nums1
                break
            if nums1[i] <= nums2[j]:
                new_list.append(nums1[i])
                i+=1
                if i == len(nums1):
                    for n_j in range(j,len(nums2)):
                        new_list.append(nums2[n_j])
                    break
            else:
                new_list.append(nums2[j])
                j+=1
                if j == len(nums2):
                    for n_j in range(i,len(nums1)):
                        new_list.append(nums1[n_j])
                    break
        len_new = len(new_list)
        # print(len_new)
        if len_new == 0: 
            raise(ValueError)
        if len_new % 2 ==0 :
            return (new_list[int((len_new-1)/2)] + new_list[int((len_new-1)/2)+1] ) /2.0
        return new_list[int(len_new/2)]
    def FindMedianBinary(self,nums1,nums2):
        m,n = len(nums1),len(nums2)
        if n < m:
            nums1,nums2,m,n = nums2,nums1,n,m


        max_inf =  float('inf')
        min_inf = float('-inf')

        h0 = 0
        hi = m





        while h0<=hi:

            i = int((h0+hi)/2)
            j = int((m+n+1)/2) - i
            left_1_max = min_inf if i == 0 else nums1[i-1]
            left_2_max = min_inf if j == 0 else nums2[j-1]
            right_1_min = max_inf if i == len(nums1) else nums1[i]
            right_2_min = max_inf if j == len(nums2) else nums2[j]

            if max(left_1_max,left_2_max) <= min(right_1_min,right_2_min):
                if (m+n)%2 == 1:
                    return float(max(left_1_max,left_2_max))
                else:
                    return (max(left_1_max,left_2_max)+ min(right_1_min,right_2_min))/2.0
            if left_1_max > right_2_min:
                hi = i-1
            if right_1_min < left_2_max:
                h0 = i+1
        return 0.0
        

if  __name__ == "__main__":
    nums1 = [1,2,3,3]
    nums2 = [3,4,5,5,6,7,8]
    solu = Solution()
    # median = solu.findMedianSortedArrays_force(nums1=nums1,nums2=nums2)
    median = solu.FindMedianBinary(nums1=nums1,nums2=nums2)
    print(median)

