# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        ans=None
        head=None
        while lists.count(None)!=len(lists):
            pre=[]
            for x in lists:
                if x:
                    pre.append(x.val)
            min1= min(pre)
            for i in range(len(lists)):
                if lists[i]:
                    if lists[i].val==min1:
                        print(min1)
                        if ans==None:
                            ans = ListNode(min1)
                            head = ans
                        else:
                            ans.next = ListNode(min1)
                            ans=ans.next
                        lists[i]=lists[i].next
        return head
a= Solution()
q1=ListNode(1)
q1.next=ListNode(4)
q1.next.next=ListNode(5)
q2=ListNode(1)
q2.next=ListNode(3)
q2.next.next=ListNode(4)
q3=ListNode(2)
q3.next=ListNode(6)

a.mergeKLists([q1,q2,q3])
