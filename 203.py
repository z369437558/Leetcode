class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    if head is None:
        return head
    now=head
    while head.val==val:
        head=head.next
        if head is None:
            return head
    while(now.next is not None):
        if now.next.val==val:
            next = now.next
            while next.val==val:
                next=next.next
                if next is None:
                    break
            now.next=next
        now=now.next
        if now is None:
            return head
    return head
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
removeElements(head,2)