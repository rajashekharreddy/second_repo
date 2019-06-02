class Solution:
    def thirdMax(self, nums):
        nums = set(nums)
        for _ in range((2, 0)[len(nums) < 3]):
        	print(_)
        	nums.remove(max(nums))
        return max(nums)

inst1 = Solution()
print(inst1.thirdMax([2,2,1,3,2,3]))