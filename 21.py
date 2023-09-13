class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def main(list1,list2):
    chain = []
    while list1 or list2:
        if list1 and list2:
            if list1.val<list2.val:
                chain.append(list1)
                list1= list1.next
            else:
                chain.append(list2)
                list2 = list2.next
        else:
            if list1:
                chain.append(list1)
                list1= list1.next
            if list2:
                chain.append(list2)
                list2=list2.next
    for i in range(len(chain)-1):
        chain[i].next=chain[i+1]
    if len(chain)>0:
        return chain[0]
    else:
        return None
# list1=ListNode(1)
# list1.next = ListNode(2)
# list1.next.next = ListNode(4)
# list2 = ListNode(1)
# list2.next = ListNode(3)
# list2.next.next = ListNode(5)
list1 = None
list2 = None
print(main(list1,list2))