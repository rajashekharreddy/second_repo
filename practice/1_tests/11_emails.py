class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        modified = list()
        
        for email in emails:
            
            local = email.split("@")[0]
            domain = email.split("@")[1]
            if "+" in local:
                local = local.split("+")[0]
            local = local.replace(".","")
            total = local + "@" +domain
            modified.append(total)
        print(modified)
        return len(set(modified))

inst1 = Solution()
print(inst1.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))