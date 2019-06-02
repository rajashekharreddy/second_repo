class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if s == "" or s==" ":
            return 0
        
        else:
            words = s.split(" ")
            print(words)
            no_dups = list()
            for i in range(len(words)):
                if words[i] != "":
                    no_dups.append(words[i])

            print(no_dups)
            return len(no_dups[-1])

inst1 = Solution()

print(inst1.lengthOfLastWord("b   a    "))