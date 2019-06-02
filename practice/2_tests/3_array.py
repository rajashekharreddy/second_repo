class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
        output = list()
        
        for element in queries:
            new = A[element[1]] + element[0]
            A.pop(element[1])
            A.insert(element[1], new)
            evens = 0
            for j in A:
                if j % 2 == 0:
                    evens = evens + j
            output.append(evens)
        return output


inst1 = Solution()
print(inst1.sumEvenAfterQueries([1,2,3,4],[[1,0],[-3,1],[-4,0],[2,3]]))