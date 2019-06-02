class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        val = 0
        subs = list()
        for emp in employees:
            
            if emp[0] == id:
                
                val = emp[1]
                subs = emp[2]
        
        for emp in employees:
            
            if emp[0] in subs:
                
                val += emp[1]
        return val
                
inst1 = Solution()

print(inst1.getImportance([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1))