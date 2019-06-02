class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set(("q","w","e","r", "t", "y", "u", "i", "o", "p"))
        row2 = set(("a", "s", "d", "f", "g", "h", "j", "k", "l"))
        row3 = set(("z", "x", "c", "v", "b", "n", "m"))
        output = list()
        for word in words:
            
            word_set = set(list(word.lower()))
            
            print(word_set)

            if word_set.issubset(row1) or word_set.issubset(row2) or word_set.issubset(row3):

                output.append(word)
        return output


inst1 = Solution()

inst1.findWords(["Hello", "Alaska", "Dad", "Peace"])