class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        retList=set()
        for x in range(0,len(nums)):
            for y in range(x+1,len(nums)):
                for z in range(y+1,len(nums)):
                    if nums[x]+nums[y]+nums[z]==0:                    
                        retList.add(tuple([nums[x],nums[y],nums[z]]))
        return [list(x) for x in retList]