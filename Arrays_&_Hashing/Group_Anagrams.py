class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []

        dict = {}
        for i in range(len(strs)):
            str = ''.join(sorted(strs[i]))
            print(str)
            if str in dict:
                dict[str].append(strs[i])
            else:
                dict[str] = [strs[i]]
        
        for v in dict.values():
            output.append(v)
        return output

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        dict2 = {}
        count = []

        countChar = []
        full_list = []
        output = []
        for s in strs:
            for c in s:
                count.append(c)
            for char in sorted(count):
                dict[char] = dict.get(char, 0) + 1
            count = []

            for k, v in dict.items():
                string = str(v) + k
                countChar.append(string)
            full_list.append(countChar)
                                                                                                 

            countChar = []
            dict = {}

        for i in range(0,len(full_list)):
                dict2[tuple(full_list[i])] = dict2.get(tuple(full_list[i]), '') + strs[i] + ' ' 

        for k, v in dict2.items():
            v = v.split(' ')
            output.append(v[0:(len(v) - 1)])

        return output