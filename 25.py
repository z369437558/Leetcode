class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k: int):
        def reverse(head,t):
            if t==1:
                return head
            now = head
            for i in range(t-1):
                now=now.next
                if not now:
                    return head
            end = now
            end.next = reverse(head,t-1)
            return end
        head1 = ListNode(0)
        head1.next = head
        head = head1
        while head.next:
            pre=head
            head=head.next
            now = head
            for i in range(k):
                if now:
                    now = now.next
                else:
                    return head1
            end = now
            pre.next = reverse(head,k)
            head.next=end
        return head1
a = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
a.reverseKGroup(head,3)