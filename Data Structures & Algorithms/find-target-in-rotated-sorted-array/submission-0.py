class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0 
        right = len(nums)-1

        if target in nums:
            for i,x in enumerate(nums):
                if x == target:
                    return i
        else:
            return -1