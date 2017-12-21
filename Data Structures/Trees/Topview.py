"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def leftnode(root):
    if root == None:
        return
    leftnode(root.left)
    print(root.data),
    
def rightnode(root):
    if root == None:
        return
    print(root.data),
    rightnode(root.right)
    

def topView(root):
  #Write your code here
    if root == None:
        return
    leftnode(root.left)
    print(root.data),
    rightnode(root.right)
    
    
    
            
       