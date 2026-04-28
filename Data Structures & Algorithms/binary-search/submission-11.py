class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        length = len(nums)

        left, right  = 0, length-1

        index = (left+right)//2 
        while left<=right:
            
            print(left,right,index)
            if nums[index] == target:
                return index
            elif nums[index] < target : 
                left = index+1
            elif nums[index] > target:
                right = index-1
            index = (left+right)//2 


        return -1