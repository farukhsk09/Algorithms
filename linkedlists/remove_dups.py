class Node:
    def ___init__(self,d):
        self.d=d
        self.next = None
    
class SLinkedList:
    def __init__(self):
        self.head= None
    def __init__(self,head,d):
        self.head= head
        self.d=d
    
v = SLinkedList()
v.head=Node(4)

