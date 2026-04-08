class Node:
    def __init__(self,info,next=None):
        self.data= info
        self.next=next

class SingleLinkedList:
    def __init__(self,head=None):
        self.head=head

    def insertAtEnd(self,val):
        temp= Node(val)
        if(self.head!=None):
            t1=self.head
            while(t1.next!=None):
                t1=t1.next
            t1.next=temp
        else:
            self.head=temp
    
    def insertAtBeg(self,val):
        temp=Node(val)
        if(self.head!=None):
            t1=self.head
            temp.next=t1
            self.head=temp
        else:
            self.head=Node(val)

    def printLL(self):
        temp=self.head
        while temp.next!=None:
            print(temp.data)
            temp=temp.next
        print(temp.data)


obj=SingleLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(40)
obj.insertAtBeg(50)
obj.insertAtBeg(100)
obj.printLL()
        
