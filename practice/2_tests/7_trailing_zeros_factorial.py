class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        factorial = 1
        for i in range(1, n+1):
            factorial = i * factorial
        
        total = 0
        for j in range(len(str(factorial))-1, 0, -1):
            
            if str(factorial)[j] != "0":
                break
            
            elif str(factorial)[j] == "0":
                
                total += 1
                
                
        return total

inst1 = Solution()
print(inst1.trailingZeroes(1574))