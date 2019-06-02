

import re
class Solution:
    def mostCommonWord(self, paragraph, banned):
        para = re.sub("[^a-z ]+", " ", paragraph.lower())
        print(para)
        para = para.split()
        for a in banned:
            para = list(filter(lambda x: x != a, para))
        return max(set(para), key = para.count)


inst1 = Solution()

print(inst1.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))