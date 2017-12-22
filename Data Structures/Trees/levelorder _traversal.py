"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def levelOrder(root):
   #Write code Here
    if root == None:
        return
    arry = []
    arry.insert(0,root)
    
    while len(arry) > 0:
        current = arry.pop()
        print(current.data),
        if current.left != None:
            arry.insert(0,current.left)
        if current.right != None:
            arry.insert(0, current.right)
        