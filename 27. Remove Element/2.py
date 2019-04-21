class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #__slots__ = ('count')

        count=len(nums)
        i=0
        while i<count:
            if val==nums[i]:
                count=count-1
                nums[i],nums[count]=nums[count],nums[i]
            else:
                i=i+1
        return count
#Runtime: 36 ms
#Memory Usage: 13.2 MB
#Q:How to reduce memory usage
