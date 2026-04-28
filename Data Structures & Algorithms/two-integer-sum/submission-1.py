class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap= {}
        index =0
        for x in nums:
            val = target -x 
            if x in hashmap:
                return [hashmap[x],index]
            hashmap[val] = index

            index += 1
            print(hashmap)


        return []
        