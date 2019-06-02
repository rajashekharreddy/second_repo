class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            
            return 0
        
        else:
            
            for i in range(len(haystack)):
                print(haystack[i:i+len(needle)])
                if needle == haystack[i:i+len(needle)]:
                    
                    return i
                
            return -1


inst1 = Solution()

print(inst1.strStr("hello", "ll"))