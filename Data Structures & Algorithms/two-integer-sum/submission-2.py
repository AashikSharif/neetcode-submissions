class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap= {}
        index =0
        for x in nums:
            val = target -x 
            if val in hashmap:
                return [hashmap[val],index]
            hashmap[x] = index

            index += 1
            print(hashmap)


        return []
        