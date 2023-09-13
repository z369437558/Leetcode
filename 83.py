
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        now = head
        while now is not None:
            if now.next is None:
                return head
            if now.val!= now.next.val:
                now = now.next
            else:
                now.next = self.findNextDiff(now)
        return head
            

    def findNextDiff(self,now):
        while (now.next.val==now.val):
            now= now.next
            if now is None:
                return now
        return now.next

ans = Solution()
head =  ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
ans.deleteDuplicates(head)