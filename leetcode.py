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

    def printLL(self):
        temp = self.head
        while temp != None:  # FIXED: handles single node
            print(temp.data, end=" → ")
            temp = temp.next
        print("NULL")

    def reverseList(self,head):
        prev,curr=None,head
        while(curr!=None):
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev 
    
    def setHead(self, new_head):  # Helper to update self.head
        self.head = new_head

obj=SingleLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtEnd(50)
obj.printLL()

new_head = obj.reverseList(obj.head)
obj.setHead(new_head)
obj.printLL()

