class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        temp = 0
        
        for num in nums:
            
            if num == 1:
                
                temp += 1
                
            else:
                
                if temp > count:
                    
                    count = temp
                temp = 0
            print(count, temp)
            
        return count if count > temp else temp


inst1 = Solution()

print(inst1.findMaxConsecutiveOnes([1,0,1,1,1,0,1]))