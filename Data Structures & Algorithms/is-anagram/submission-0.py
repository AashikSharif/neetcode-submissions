class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1, str2= {}, {}
        for x in s:
            if x in str1:
                str1[x] += 1
            else:
                str1[x] =1
    
        for x in t:
            if x in str2:
                str2[x] += 1
            else:
                str2[x] =1
        
        return str1==str2