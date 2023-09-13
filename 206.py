# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    ans = fun(head)
    return ans
def fun(head):
    if head==None or head.next == None:
        return head
    ans = fun(head.next)
    head.next.next=head
    return ans
    
head=ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head = reverseList(head)
print('111')