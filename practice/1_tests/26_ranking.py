class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranks = sorted(nums, reverse=True)
        rank_dict = dict()
        
        for i in range(len(nums)):
            
            if i == 0:
                rank_dict[ranks[i]] = "Gold Medal"
            elif i == 1:
                rank_dict[ranks[i]] = "Silver Medal"
            elif i == 2:
                rank_dict[ranks[i]] = "Bronze Medal"
            else:
                rank_dict[ranks[i]] = str(i+1)
        
        for i in range(len(nums)):

            nums[i] = rank_dict[nums[i]]

        return nums

inst1 = Solution()
print(inst1.findRelativeRanks([10,3,8,9,4]))

import sys
print(sys.version)