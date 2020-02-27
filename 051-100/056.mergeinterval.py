class Solution:
    def merge(self, intervals):
        
        if len(intervals) < 2:
            return intervals

        sorted_intervals  = sorted(intervals,key=lambda x: x[0])

        print(sorted_intervals)

        out_merged = []
        pre_interval = sorted_intervals[0]

        for i in range(1,len(sorted_intervals)):
            # if sorted_intervals[i] with pre_interval:
            # pre_interval = concate(sorted_intervals,pre_interval)
            # else:
            # out_merged.append(pre_)
            # pre_ = sorted_[i]
            print(sorted_intervals[i])
            print(pre_interval)
            if sorted_intervals[i][0] <= pre_interval[1]:
                pre_interval = [min(pre_interval[0],sorted_intervals[i][0]),max(pre_interval[1],sorted_intervals[i][1])]

            else:
                out_merged.append(pre_interval)
                pre_interval = sorted_intervals[i]
            if i == len(sorted_intervals) - 1:
                    out_merged.append(pre_interval)

        return out_merged


if __name__ == "__main__":
    
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(Solution().merge(intervals))