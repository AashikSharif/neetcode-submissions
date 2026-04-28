class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        if len(nums) ==1: 
            return nums[0]
        
        ret = 0
        for x in nums:
            ret = ret ^ x
        
        return ret
            