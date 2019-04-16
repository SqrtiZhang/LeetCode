class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int size=nums.size();
        vector<int> a;
        for(int i=0;i<size;i++)
            for(int j=i+1;j<size;j++)
            {
                if(nums[i]+nums[j]==target)
                {
                    a.push_back(i);
                    a.push_back(j);
                    return a;
                }
            }
    }
};

//Runtime: 84 ms
//Memory Usage: 1.4 MB
//Brute Force O(n^2)
