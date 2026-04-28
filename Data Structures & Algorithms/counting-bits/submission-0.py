class Solution:
    def countBits(self, n: int) -> List[int]:
        newlist = [0]
        count = 0
        for x in range(1,n+1):
            while x!=0:
                if x < len(newlist):
                    count += newlist[x]
                    x=0
                    break

                if x%2==1:
                    count+=1
                x = x//2
            
            newlist.append(count)
            count=0
        return newlist