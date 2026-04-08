class Node:
    def __init__(self,value=None):
        self.data=value
        self.next=None
        self.prev=None

class DoublyLL:
    def __init__(self,head=None):
        self.head=head

    def insertAtEnd(self,val):
        temp=Node(val)
        if(self.head!=None):
            t1=self.head
            while(t1.next!=None):
                t1=t1.next
            t1.next=temp
            temp.prev=t1
        else:
            self.head=temp

    def insertAtBeg(self,val):
        temp=Node(val)
        if(self.head!=None):
            t1=self.head
            temp.next=t1
            t1.prev=temp
            temp.prev=None
            self.head=temp
        else:
            self.head=temp

    def insertAtMid(self,val,x):
        temp=Node(val)
        t1=self.head
        while(t1.next!=None):
            if(t1.data==x):
                t2=t1.next
                t1.next=temp
                temp.prev=t1
                temp.next=t2
                t2.prev=temp
            t1=t1.next
        if(t1.data==x):
            t1.next=temp
            temp.prev=t1

    def delLL(self,val):
        temp=self.head
        if(temp.data==val):
            temp.next.prev=None
            self.head=temp.next
            temp.next=None
            return
        while(temp.next!=None):
            if(temp.data==val):
                temp.prev.next=temp.next
                temp.next.prev=temp.prev
            temp=temp.next
        if(temp.data==val):
            temp.prev.next=None
            temp.prev=None
        

    def printLL(self):
        t1=self.head
        while(t1!=None):
            print(t1.data,end=" -- ")
            t1=t1.next
        print("NULL")
    
obj=DoublyLL()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBeg(100)
obj.insertAtBeg(200)
obj.insertAtMid(50,20)
obj.insertAtMid(150,30)
obj.insertAtMid(120,20)
obj.delLL(30)
obj.delLL(150)
obj.delLL(200)
obj.delLL(100)
obj.printLL()