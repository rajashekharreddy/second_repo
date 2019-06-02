class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        for i in range(1, n+1):
            
            n = n - i
            if n <= 0:
                break
            total = total + 1
        return total

inst1 = Solution()
print(inst1.arrangeCoins(888))

"""
X
X X
X X X
X X X X
X X X X X

"""