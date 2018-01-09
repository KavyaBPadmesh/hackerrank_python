"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
        if position == 0:
            if head == None:
                newnode = Node(data,None)
                head = newnode
                return head
            else:
                newnode = Node(data,head)
                head = newnode
                return head    
        else:
            current = head
            counter = 0
            while (counter < position-1):
                current = current.next
                counter += 1
            newnode = Node(data, current.next)
            current.next = newnode
            return head

        
            
            
  
  
  
  
  
  
  
  
  
  
