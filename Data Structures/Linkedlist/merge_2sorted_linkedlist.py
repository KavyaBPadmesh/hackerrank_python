"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def MergeLists(headA, headB):
    if headA == None:
        return headB
    elif headB == None:
        return headA
    elif headA.data > headB.data:
        currentB = headB
        headB = headB.next
        currentB.next = headA
        headA = currentB
        return headA
    else:
        currentA = headA
        currentB = headB
        while (currentA.next and currentB):
            if currentA.next.data < currentB.data:
                currentA = currentA.next
            else:
                newnode = currentB
                currentB = currentB.next
                newnode.next = currentA.next
                currentA.next = newnode
                currentA = currentA.next
        if currentB != None:
            currentA.next = currentB
        return headA       
            