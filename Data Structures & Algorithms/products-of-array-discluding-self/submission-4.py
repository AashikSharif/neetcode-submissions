class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 not in nums:
            prod=1
            for x in nums:
                prod = prod*x
            for i,x in enumerate(nums):
                nums[i]=int(prod/nums[i])
            return nums
        else:
            prod = 1
            flag=0
            for x in nums:
                if x == 0:
                    if flag==1:
                        prod=0
                    flag=1
                    
                    continue
                prod = prod*x
            print(prod)
            for i,x in enumerate(nums):
                if nums[i]!=0:
                    nums[i]=0
                    continue
                nums[i]=prod
            return nums
