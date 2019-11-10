class Solution:
    def groupAnagrams(self, strs):
        mode_dict = {}
        for s_item in strs:
            mode = str(sorted(s_item))
            if mode not in mode_dict.keys():
                mode_dict[mode] = [s_item]
            else:
                mode_dict[mode].append(s_item)
        # print(mode_dict.values)

        out_ = []
        for v in mode_dict.values():
            out_.append(v)
        return out_

if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs=strs))

        