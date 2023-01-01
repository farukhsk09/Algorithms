# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p3=None
        newHead=None
        remainder=0
        while(l1!=None and l2!=None):
            if p3==None:
                value =(l1.val+l2.val)%10
                if l1.val+l2.val >= 10:
                    remainder = 1
                else:
                    remainder=0
                p3=ListNode(value)
                newHead=p3
            else:
                value = (l1.val + l2.val + remainder)%10
                if l1.val+l2.val+remainder >= 10:
                    remainder = 1
                else:
                    remainder=0
                newVal = ListNode(value)
                p3.next=newVal
                p3=p3.next
            l1=l1.next
            l2=l2.next
        if l2!=None:
            while(l2!=None):
                value = (l2.val + remainder)%10
                if l2.val+remainder >= 10:
                    remainder = 1
                else:
                    remainder=0
                newVal = ListNode(value)
                p3.next=newVal
                p3=p3.next
                l2=l2.next
        if l1!=None:
            while(l1!=None):
                value = (l1.val + remainder)%10
                if l1.val+remainder >= 10:
                    remainder = 1
                else:
                    remainder=0
                newVal = ListNode(value)
                p3.next=newVal
                p3=p3.next
                l1=l1.next
        if remainder == 1:
            newVal = ListNode(remainder)
            p3.next=newVal
            p3=p3.next
        return newHead
