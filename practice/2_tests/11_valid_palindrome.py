class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        given = s.split(" ")
        given = list(map(lambda x : x.lower().strip(" :,"), given))
        input_str = "".join(given)
        print(input_str, input_str[::-1])
        return input_str == input_str[::-1]
        

inst1 = Solution()

#print(inst1.isPalindrome("A man, a plan, a canal: Panama"))
print(inst1.isPalindrome("ab@a"))
