# 0,1,1,2,3,5,8,13

# class Solution(object):
#     fibs = dict()
#     def fib(self, N):
#         """
#         :type N: int
#         :rtype: int
#         """
#         print(Solution.fibs)
#         if N==1:
#             Solution.fibs[1] = 0
#             return 0
        
#         elif N==2:
#             Solution.fibs[2] = 1
#             return 1

#         else:
        
#             if N in Solution.fibs:
#                 return Solution.fibs[N]

#             else:
#                 Solution.fibs[N] = self.fib(N-1) + self.fib(N-2)
#                 return Solution.fibs[N]


class Solution(object):

    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        fibs = [0,1]
        
        for i in range(2,N):
            
            fibs.append(fibs[-1]+fibs[-2])
            print(fibs)
        
        return fibs[N-1]

inst1 = Solution()

print(inst1.fib(3))