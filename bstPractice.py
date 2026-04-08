class Node:
    def __init__(self,value):
        self.data=value
        self.right=None
        self.left=None

def insert(root,value):
    if(root==None):
        return Node(value)
    if(value<root.data):
        root.left=insert(root.left,value)
    else:
        root.right=insert(root.right,value)
    return root

def search(root,value):
    if(root==None):
        print("Element not found!!")
        return
    if(root.data==value):
        print("Element Found.")
        return
    if(value<root.data):
        search(root.left,value)
    elif(value>root.data):
        search(root.right,value)

def get_successor(root):
    root=root.right
    while(root.left!=None and root!=None):
        root=root.left
    return root


def delete(root,value):
    if(root==None):
        print("Value is invalid!!")
        return root
    if (value<root.data):
        root.left=delete(root.left,value)
    elif(value>root.data):
        root.right=delete(root.right,value)
    else:
        if(root.left==None):
            return root.right
        if(root.right==None):
            return root.left
        else:
            succ=get_successor(root)
            root.data=succ.data
            root.right=delete(root.right,succ.data)
    return root


def inOrder(root):
    if(root!=None):
        inOrder(root.left)
        print(root.data,end=" ")
        inOrder(root.right)


root=None
root=insert(root,10)
root=insert(root,20)
root=insert(root,5)
root=insert(root,15)
root=insert(root,25)
root=insert(root,17)
inOrder(root)
search(root,10)
search(root,30)
delete(root,10)
delete(root,25)
inOrder(root)
