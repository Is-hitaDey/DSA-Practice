def isEmpty(stack):
        if len(stack.s)==0:
            return True
        else:
            return False
class stack:
    
    def __init__(self):
        self.s=[]

    def length(self):
        return len(self.s)
    
    def push(self,value):
        self.s.insert(0,value)

    def peek(self):
        if isEmpty(self):
             raise Exception("Stack is Empty")
        else:
             return self.s[0]
    
    def pop(self):
         if isEmpty(self):
              raise Exception("Stack is Empty! Nothing to pop...")
         else:
              return self.s.pop(0)
         
stk=stack()
stk.push(10)
stk.push(20)
print(stk.peek())
