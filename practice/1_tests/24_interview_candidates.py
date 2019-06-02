class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        
        summ = 0
        sort_D = sorted(costs,key=lambda x:x[0]-x[1])
        print(sort_D)
        for i in xrange(len(costs)//2):
            summ += sort_D[i][0]+sort_D[-i-1][1]
        return summ


sol1 = Solution()

print(sol1.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))