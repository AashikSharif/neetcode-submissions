class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x=0
        y=len(numbers)-1

        for _ in range(len(numbers)): 
 
            if numbers[x]==target-numbers[y]:
                return [x+1,y+1]
            elif numbers[x]<target-numbers[y]:
                x+=1
            elif numbers[x]>target-numbers[y]:
                y-=1
                