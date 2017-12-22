"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def topView(root):
  #Write your code here
    if root == None:
        return
    
    arry = str(root.data) + ' '
    current = root
    
    while current.left != None:
        current = current.left
        arry = str(current.data) + ' ' + arry
    while root.right != None:
        root = root.right
        arry += str(root.data) + ' '
    print(arry)
    
    
            
       