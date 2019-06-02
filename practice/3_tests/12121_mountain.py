class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            
            return False
        
        else:
            peak = 0
            for i in range(len(A)-1):
                
                if A[i] >= A[i+1]:
                    peak = i
                    break

            print(i)
            if i == 0:
                return False
            for j in range(i, len(A)-1):

                if A[j] <= A[j+1]:

                    return False

            return True

s1 = Solution()

print(s1.validMountainArray([9,8,7,6,5,4,3,2,1,0]))