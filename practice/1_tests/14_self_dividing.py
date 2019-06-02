class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        selfdivid = list()
        for num in range(left, right+1):
            
            ind = [int(x) for x in str(num)]

            if ind.count(0) > 0:
                continue
                
            for element in ind:
                
                if num % element != 0:
                    break
            selfdivid.append(num)
        return selfdivid

inst1 = Solution()
print(inst1.selfDividingNumbers(1,3))