"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if head == None:
        return
    else:
        slownode = head
        fastnode = head
        while fastnode.next != None and fastnode.next.next!=None:
            slownode = slownode.next
            fastnode = fastnode.next.next
            if slownode == fastnode:
                return True
        return False