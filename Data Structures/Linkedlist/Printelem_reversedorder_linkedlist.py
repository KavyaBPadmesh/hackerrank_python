"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""
def ReversePrint(head):
    if head == None:
        return
    else:
        data = []
        current = head
        while current:
            data.append(current.data)
            current = current.next
        for i in reversed(data):
            print(i)
        
  
  
  
    
