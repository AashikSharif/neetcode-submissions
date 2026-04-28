class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        print(res)
        for s in strs:
            x = ''.join(sorted(s))
            print(x)
            if x in res:
                res[x].append(s)
            else:
                res[x]=[s]
        
        return res.values()           
            


    def isAnagram(str1,str2):
        dict1,dict2={},{}

        for x in str1: 
            if x not in dict1:
                dict1[x]=1
            else:
                dict1[x] += 1

        for x in str2: 
            if x not in dict2:
                dict2[x]=1
            else:
                dict2[x] += 1
        
        return dict1==dict2
