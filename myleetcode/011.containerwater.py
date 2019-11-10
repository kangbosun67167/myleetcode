# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

class Solution:
    def LocationOfLine(self,list_height):
        len_list = len(list_height)
        left_location = 0
        right_location = len_list-1
        max_area = (len_list-1) * min(list_height[left_location],list_height[right_location])
        while left_location < right_location:
            left_height = list_height[left_location]
            right_height = list_height[right_location]
            if left_height <= right_height:
                left_location += 1
                left_height = list_height[left_location]
            else:
                right_location -= 1
                right_height = list_height[right_location]

            area = (right_location-left_location) * min(left_height,right_height)
            # print(area)
            if area > max_area:
                max_area = area
        return max_area

if __name__ == "__main__":
    
    s = [10,14,10,4,10,2,6,1,6,12]
    solu = Solution()
    print(solu.LocationOfLine(s))