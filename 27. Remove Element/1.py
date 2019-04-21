class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=len(nums)
        i=0
        while i<count:
            if val==nums[i]:
                count=count-1
                nums.pop(i)
            else:
                i=i+1
        return count
       

#Runtime: 52 ms
#time waste:pop
#Memory Usage: 13.2 MB
