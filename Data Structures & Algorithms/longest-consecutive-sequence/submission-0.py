class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        print(nums)
        length = 1
        return_len = 0
        if len(nums)==1:
            return 1
        elif len(nums)==0:
            return 0
        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                length += 1
            else:
                length =1
            if length > return_len:
                return_len = length
            print(i,length)

                
        return return_len
