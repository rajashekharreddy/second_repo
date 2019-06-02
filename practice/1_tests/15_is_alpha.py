class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        given = list()
        for letter in licensePlate:
            if letter.isalpha():
                given.append(letter.lower())
        print(sorted(given))
        for word in words:
            #print(word, sorted(list(word)), sorted(given))
            #if all(x in sorted(given) for x in sorted(list(word))):
            #    return word
            for i in sorted(given):

                if i not in word:

                    break
            return word

inst1 = Solution()

print(inst1.shortestCompletingWord("1s3 PSt", ["step", "steps", "stripe", "stepple"] ))