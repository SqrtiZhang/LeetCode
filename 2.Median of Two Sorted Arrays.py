class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1=len(nums1)
        len2=len(nums2)
        if len1<len2:
            return self.findMedianSortedArrays(nums2, nums1)#make sure that nums2 is the shorter one in order to save time
        
        low=0
        high=len2*2
        
        while low<=high:
            mid2=int((low+high)/2)
            mid1=len1+len2-mid2
            #eage case
            l1= -(sys.maxsize-1) if mid1==0 else nums1[int((mid1-1)/2)]
            l2= -(sys.maxsize-1) if mid2==0 else nums2[int((mid2-1)/2)]
            r1= sys.maxsize if mid1==len1*2 else nums1[int(mid1/2)]
            r2= sys.maxsize if mid2==len2*2 else nums2[int(mid2/2)]
    
            if l1>r2: #which means that nums1 lower half is too big
                low=mid2+1
            elif l2>r1:
                high=mid2-1
            else:
                return (max(l1,l2)+min(r1,r2))/2
#Runtime: 60 ms
#Memory Usage: 13.2 MB

#recursion in class needs self.
#remember in python, it doesn't require variable declaration, which means if c=a/b,c is floating-point type instead of  interger type
#a good way to deal with string:[# 1 # 2 # 3 # (4/4) # 5 #]  
#Manacher‘s Algorithm
