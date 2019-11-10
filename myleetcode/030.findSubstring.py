# You are given a string, s, and a list of words, words, that are all of the same length. 
# Find all starting indices of substring(s) in s that is a concatenation of each word in words
#  exactly once and without any intervening characters.

 

# Example 1:

# Input:
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        list_maps = {}
        word_len  = len(words[0])
        out_index = []
        times_map,len_words = self.Timesmap(words)
        # print(times_map)
        # print(len(s)-word_len)
        for i in range(len(s)-word_len + 1):

            # print(s[i:i+word_len])
            if s[i:i+word_len] in words:
                if s[i:i+word_len] not in list_maps:
                    list_maps[s[i:i+word_len]] = list()
                list_maps[s[i:i+word_len]].append(i)
                print(list_maps)
                if len(list_maps) == len_words:
                    value_list = [] 
                    
                    for k,v in list_maps.items():
                        value_list.extend(v[-times_map[k] :])
                    # value_list = [i for i in value_list_list]
                    # print(values)
                    print(value_list)
                    value_list = sorted(value_list)
                    if len(value_list) == len(words) and  self.Isit(value_list,word_len) and value_list[0] not in out_index:
                        out_index.append(value_list[0])
        return out_index
    def Isit(self,v_list,v_error):
        if len(v_list) == 1:
            return True
        if len(v_list)<2:
            return False
        for i in range(1,len(v_list)):
            if v_list[i] - v_list[i-1] != v_error:
                return False
        return True
    def Timesmap(self,words_list):
        times_map = {}
        len_words = 0
        for item in words_list:
            if item not in times_map:
                times_map[item] = 1
                len_words += 1
            else:
                times_map[item] += 1
        return times_map,len_words

    def newfinder(self, s, words):
        if not s or not words:
            return []
        len_word =  len(words[0])
        len_sub = len(words) * len(words[0])
        out_list = []
        for sub_i in range(len(s)-len_sub+1):
            sub_s = []
            tmp_i = sub_i
            while tmp_i < sub_i + len_sub:
                
                sub_s.append(s[tmp_i:tmp_i+len_word])
                tmp_i += len_word
            # print(sub_i,sub_s)
            if self.Timesmap(words) == self.Timesmap(sub_s):
                # print("!!!")
                out_list.append(sub_i)
        return out_list
if __name__ == "__main__":

    s = "fxgpwfxehfushbiwzqbrxbrjmrsprlkzlqohynnfsjxbkhajxddweuftoakfnugamwjklwsdgrhszjeyohvudcprezzstfsiccunamtgecbfnffbmcxphnjlmidinwqramhazcjfekmtptudwtufgdqtludbsvsuhbuiddpjpbcexyjvseayhqtvmwwgtqadsxlxabhqejwdigyamyavruqdsmmofmrxjcwmfdemnapviovuovqfrilmvxacjrbvvxhbblponejyuguldkqxvdjsajumcvhxsqytdpjswuqqaldgxwfszokazeobbxyunzpsozkmtdfwoienejggzsgyzwbatzwiamarnmdirigftkvxvbduvlsuhvvcxrkxfmqsbwdsgjazwvxrycmtqgozclczcmykbrccnhutrwtprsgpwulmdbofmqgqegafxfhkmeefazusrdjpxwcaxqhlincmwestlzeydkfgjcycfjrcgvfdnmrvctkyzetlfxlljqrsupwzyqegnjmbxdybwkzvotiustfcmwwglvgllksavgbsjcufovcdqlxlgcpsalznifatruumaxgjbcqqytvqgsbmwsfyeelmllicgeogduqhxgxxbspjmtwkldirjveugowoumxxipehxdgzxwklpgxclfuuayojomziawhjloqjrzkrvucmbaoohijkizvymuimrqxeeqnxpxqmsvyvxojexuqhungiiowbgufmkvkzsanmvlhsztzynrihfqrpgosnixzuulvnoizlvjgwehvryfbfvsubimqqmskgdhvtpxfkglhksedsjgygzujhjcavumdzuztlwywejdqdjvvucvadqlmznmwhbzhvaciyaeeljwqssloujozzclapywzbxiyykgwmlbxwxnrrafnjwmkyympyiozgwxgifeuqftpfggyjnmulyhjwtzucpvkouswawtsemhlvpjefvaqwhasbbpfsmrghjfhhyblmjwhailfdmwbvywwbndtzwcifjrnhtatezdehqmmekoaikylxcgyaihgryvarxwvwbcdroqwyewiqutnyblzmshfteikbeiyhkdyatuyzqipndeneqoqkxwfdgsfmaftmirmemmdeuvtzzjdrzwexujaabhmdofpzwddkrgpldikdtqwtoaqiksincwtqbipzoukfdbtglfjfxgyliqtukdimzbfclwcbrmhuncaahmffudqcvmxgphspkztxwvznjgjyilzrxewrkpwfbvlscghofdldyksksbianjumqsgahchkxvdbbmpipcmqngafikixucjmwpoetvqsqtttikcxnqncwphgardwtpkseywyvosokmhsylrndhpawziyqmwmbgehgchcqaqaoxsmlkcotrqpqzqhnmtovxxbbhdrhvsxvmlgynurfljxmzezlzpiymkztprcllbgznmaaithvcfhbjgplxxjkjlfzekkrlsqagqbokkmopvsbehmbgxnsivrmfddsvwvbowraifpybhzhqniymwqvtjjampsjlpkbnecwlrumavtskeqwcjtvsdvfupoffbishkosdkhffcxrgooizhdrmywgqnnvqwnxiepmoyrwbrnhhdqglvxxwwgmjtjzpyyycpmtofrpweydkqjvmhukfcwowhpnfnnkczdqhuhdaghkwshkbeuggswczlshyfrdhuvoqdtslcdhvmuyqofxhbbintpnbgskcoyuttngwqptcjrvywshavpprhcsnxesnemgxzotrdowngrlelseijtzqytgxxykbmsbogwfjlbytujxhdeqpzrhzlnwknioaapoilvswzqpvcpd"
    words = ["fnffbmcxphnjlmidinwqramhazc","jfekmtptudwtufgdqtludbsvsuh","buiddpjpbcexyjvseayhqtvmwwg","tqadsxlxabhqejwdigyamyavruq","dsmmofmrxjcwmfdemnapviovuov","qfrilmvxacjrbvvxhbblponejyu","guldkqxvdjsajumcvhxsqytdpjs","wuqqaldgxwfszokazeobbxyunzp","sozkmtdfwoienejggzsgyzwbatz","wiamarnmdirigftkvxvbduvlsuh","vvcxrkxfmqsbwdsgjazwvxrycmt","qgozclczcmykbrccnhutrwtprsg","pwulmdbofmqgqegafxfhkmeefaz","usrdjpxwcaxqhlincmwestlzeyd","kfgjcycfjrcgvfdnmrvctkyzetl","fxlljqrsupwzyqegnjmbxdybwkz","votiustfcmwwglvgllksavgbsjc","ufovcdqlxlgcpsalznifatruuma","xgjbcqqytvqgsbmwsfyeelmllic","geogduqhxgxxbspjmtwkldirjve","ugowoumxxipehxdgzxwklpgxclf","uuayojomziawhjloqjrzkrvucmb","aoohijkizvymuimrqxeeqnxpxqm","svyvxojexuqhungiiowbgufmkvk","zsanmvlhsztzynrihfqrpgosnix","zuulvnoizlvjgwehvryfbfvsubi","mqqmskgdhvtpxfkglhksedsjgyg","zujhjcavumdzuztlwywejdqdjvv","ucvadqlmznmwhbzhvaciyaeeljw"]

    print(Solution().newfinder(s,words))