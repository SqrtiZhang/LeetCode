class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        maxarea=0;
        right=len(height)-1;
        while(left<right):
            maxarea=max(maxarea,min(height[left],height[right])*(right-left))
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        return maxarea
#very easy^U^
#Runtime: 68 ms
#Memory Usage: 14.5 MB
