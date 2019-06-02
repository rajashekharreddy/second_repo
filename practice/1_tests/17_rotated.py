class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        
        for i in range(len(A)):
            
            mod = A[i+1:] + A[0:i+1]
            print(mod, B)
            
            if mod == B:
                
                return True
        return False

inst1 = Solution()
print(inst1.rotateString('""','""'))