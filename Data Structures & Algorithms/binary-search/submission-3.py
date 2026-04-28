class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        length = len(nums)

        left, right  = 0, length
        inc =0
        index = (left+right)//2 
        while left != index or right !=index:
            index = (left+right)//2 
            print(left,right,index)
            if nums[index] == target:
                return index
            elif nums[index] < target : 
                left = index
            elif nums[index] > target:
                right = index

            if inc ==10 : 
                break
            else:
                inc+=1
            

        return -1