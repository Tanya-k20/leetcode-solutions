class Solution:
    def groupAnagrams(self, strs):
        dic={}
        for w in strs:
            key=''.join(sorted(w))
            if key not in dic:
                dic[key]=[]
            dic[key].append(w)
        return list(dic.values())


        