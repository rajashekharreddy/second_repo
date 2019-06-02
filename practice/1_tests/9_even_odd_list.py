class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        new = list()
        even = list()
        odd = list()
        for i in range(len(A)):
            
            if A[i] % 2 == 0:
                even.append(A[i])
                    
            
            else:
                odd.append(A[i])
        print(even,odd)     
        for i in range(len(A)):
            
            if i % 2 == 0:
                
                new.append(even.pop())
            else:
                new.append(odd.pop())
        return new


inst1 = Solution()
print(inst1.sortArrayByParityII([4,2,5,7]))