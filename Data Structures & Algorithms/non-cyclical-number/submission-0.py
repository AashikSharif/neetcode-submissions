class Solution:
    def isHappy(self, n: int) -> bool:
        happyset = set()
        sum = 0
        while n != 0:
            sum += (n%10)**2
            n = n // 10
            if n==0:
                if sum ==1:
                    return True
                elif sum in happyset:
                    return False
                else:
                    happyset.add(sum)
                    n=sum
                    sum = 0
        
        return False