class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        head1 = ListNode(0)
        head1.next = head
        head = head1
        while head.next:
            head = head.next
            if head.next:
                next1 = head.next  
                head.next = head.next.next
                next1.next = head
        return head1.next 
a = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
a.swapPairs(head)