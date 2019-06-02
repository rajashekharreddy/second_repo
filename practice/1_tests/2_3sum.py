class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        self.sum_array = list()
        for i in range(len(self.nums)):
            
            for j in range(i+1, len(self.nums)):
                
                for k in range(j+1, len(self.nums)):
                    
                    if nums[i]+nums[j]+nums[k] == 0:

                        if sorted([nums[i], nums[j], nums[k]]) not in self.sum_array:
                            print(sorted([[nums[i], nums[j], nums[k]]]))
                        
                            self.sum_array.append(sorted([nums[i], nums[j], nums[k]]))
        return self.sum_array

obj1 = Solution()

print(obj1.threeSum([-1,0,1,2,-1,-4]))