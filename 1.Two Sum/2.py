class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result={}
        for i in range(len(nums)):
            if nums[i] in result:
                return [result[nums[i]],i]
            else:
                result[target-nums[i]]=i
           
#one pass hash table
#Runtime: 52 ms
#Memory Usage: 14.3 MB
