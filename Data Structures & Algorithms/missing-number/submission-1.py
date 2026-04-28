class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numset = set(nums)
        n = len(nums)
    
        for x in range(0,n+1):
            if x not in numset:
                return x
        return n        