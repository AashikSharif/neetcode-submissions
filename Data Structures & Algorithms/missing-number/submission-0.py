class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        n = len(nums)
        flag = 0
        for x in nums:
            if x != flag:
                return flag
            flag+=1
        return n        