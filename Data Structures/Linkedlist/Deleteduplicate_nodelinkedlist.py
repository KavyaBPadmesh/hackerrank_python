"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def RemoveDuplicates(head):
    if head == None:
        return
    else:
        slownode = head
        fastnode = head
        head = slownode
        while fastnode.next:
            fastnode = fastnode.next
            if slownode.data == fastnode.data:
                slownode.next = fastnode.next
                fastnode = slownode
            else:
                slownode = slownode.next
        return head         
  