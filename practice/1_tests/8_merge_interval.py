class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        new_list = list()
        
        for i in range(len(intervals)-1):
            print(i)
            
            if intervals[i][1] >= intervals[i+1][0]:
                
                new_list.append([intervals[i][0], intervals[i+1][1]])
                continue
            
            else:
                
                new_list.append(intervals[i])
                
        new_list.append(intervals[-1])
        return new_list
            
inst1 = Solution()

print(inst1.merge([[1,3],[2,6],[8,10],[15,18]]))