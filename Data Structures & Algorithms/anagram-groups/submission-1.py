class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for x in strs:
            freq = [0]*26
            
            for c in x:
                freq[ord(c)-ord('a')]+=1
            if tuple(freq) not in hashmap:
                hashmap[tuple(freq)] = [x]
            else:
                hashmap[tuple(freq)].append(x)
        
        return hashmap.values()       
            


