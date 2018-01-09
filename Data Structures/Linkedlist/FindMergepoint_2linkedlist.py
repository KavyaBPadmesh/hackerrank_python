"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def FindMergeNode(headA, headB):
    currentA = headA
    currentB = headB
    while currentA.next:
        while currentB.next:
            if currentA.next.data == currentB.next.data:
                return currentA.next.data
            else:
                currentB = currentB.next
        currentB = headB
        currentA = currentA.next
  
