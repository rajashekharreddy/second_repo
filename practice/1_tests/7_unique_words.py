class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        a_list = A.split(" ")
        b_list = B.split(" ")
        output = list()
        for element in a_list:
            
            if a_list.count(element) == 1:
                if b_list.count(element) == 0:
                    output.append(element)
                    
        for element in b_list:
            
            if b_list.count(element) == 1:
                
                if a_list.count(element) == 0:
                    
                    output.append(element)
        return output

inst1 = Solution()

print(inst1.uncommonFromSentences("this apple is sweet", "this apple is sour"))