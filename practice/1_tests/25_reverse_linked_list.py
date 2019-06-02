#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return head

    def printll(self, head):
    	curr = head

    	while curr:

    		print("{}-->".format(curr.val)),
    		curr = curr.next





head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)


inst1 = Solution()
inst1.printll(head)

print(inst1.reverseList(head))
inst1.printll(head)
