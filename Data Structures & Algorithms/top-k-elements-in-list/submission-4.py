class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        #print(k)
        for x in nums:
            if x not in hashmap:
                hashmap[x]=1
            else:
                hashmap[x]+=1
        
        sortedhash=sorted(hashmap.items(), key=lambda x: x[1],reverse=True)
        print(sortedhash)
        arr = [k for k,v in sortedhash[:k]]
        
        return arr
