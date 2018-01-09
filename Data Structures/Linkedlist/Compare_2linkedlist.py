"""
 Merge two linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
    if headA == None and headB == None:
        return 1
    elif headA == None or headB == None:
        return 0 
    else:
        currentA = headA
        currentB = headB
        while (currentA and currentB):
            if currentA.data != currentB.data:
                return 0
            else:
                currentA = currentA.next
                currentB = currentB.next
        if currentA == None and currentB == None:
            return 1
        else:
            return 0