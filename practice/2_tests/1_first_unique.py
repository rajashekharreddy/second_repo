from collections import OrderedDict 

class Solution:
    def firstUniqChar(self, s: str) -> int:
        od = OrderedDict()
        for i in range(len(s)):
            od[s[i]] = (od.get(s[i], (0,i))[0]+1,i)

        print(od)
        
        for key, value in od.items():
            if value[0] == 1:
                return value[1]
            
        return -1

inst1 = Solution()

print(inst1.firstUniqChar("leetlcode"))
