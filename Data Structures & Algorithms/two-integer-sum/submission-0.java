class Solution {
    public int[] twoSum(int[] nums, int target) {
        int flag= 0; 
        int result[] = {0,1};
        for(int i=0; i<nums.length; i++)
        {
            for(int j=i+1; j<nums.length; j++)
            {
                if(i==j || i>=nums.length || j>=nums.length)
                {  flag = 1; break; }
                else  if(nums[i]+nums[j] == target)
                {
                    result[0]=i;
                    result [1]=j;
                    return result; 
                }
            }
            if(flag ==1)
                break; 
        }
        return result;

    }
}
