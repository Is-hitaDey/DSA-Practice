class Dequeue:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return len(self.items)==0
    
    def insertAtEnd(self,value):
        self.items.append(value)

    def deleteAtEnd(self):
        self.items.pop()
    
    def insertAtfront(self,value):
        self.items.insert(0,value)

    def deleteAtFront(self):
        self.items.pop(0)

    def printQ(self):
        for i in self.items:
            print(i)

q=Dequeue()
q.insertAtfront(10)
q.insertAtfront(20)
q.insertAtEnd(100)
q.insertAtEnd(120)
q.deleteAtEnd()
q.deleteAtFront()
q.printQ() 