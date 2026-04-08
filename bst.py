arr=[20,30,15,25,40,50,23]
# y=1
# while y==1 :
#     a=int(input("Enter the number:"))
#     arr.append(a)
#     y=int(input("Do you want to continue?(press 1 to  continue:"))

class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

def insert(root,value):
    if root == None:
        return Node(value)
    if (root.data==value):
        return root
    if value<root.data:
        root.left=insert(root.left,value)
    else:
        root.right=insert(root.right,value)
    return root

def search(root,value):
    if root==None:
        print("Element not found!")
        return
    if root.data==value:
        print("Element found")
        return
    if value<root.data:
        search(root.left,value)
    else:
        search(root.right,value)

def get_successor(root):
    root=root.right
    while(root!=None and root.left!=None):
        root=root.left
    return root

def delete(root,value):
    if root==None:
        return root
    if value<root.data:
        root.left=delete(root.left,value)
    elif value>root.data:
        root.right=delete(root.right,value)
    else:
        if(root.left==None):
            return root.right
        if(root.right==None):
            return root.left
        else:
            succ= get_successor(root)
            root.data=succ.data
            root.right=delete(root.right,succ.data)
    return root

def inOrder(root):
    if(root!=None):
        inOrder(root.left)
        print(root.data,end=" ")
        inOrder(root.right)
    

root=None

for i in arr:
    root=insert(root,i)

            
inOrder(root)
print("")
search(root,35) 
search(root,30)
delete(root,30)
inOrder(root)
