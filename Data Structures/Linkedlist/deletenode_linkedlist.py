"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    if head == None:
        return
    elif position == 0:
        head = head.next
        return head
    else:
        current = head
        counter = 0
        while current.next:
            if (counter+1) == position:
                current.next = current.next.next
                return head
            else:
                current = current.next
                counter +=1
                
                
            
  