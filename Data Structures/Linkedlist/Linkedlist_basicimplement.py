class node(object):
     def __init__(self,data,nextnode):
         self.data = data
         self.next = nextnode
         
         
class linkedlist(object):
    def __init_(self,data):
        self.head = None
        self.tail = None
        
    def getsize(self):
        counter = 0
        current = self.head
        while (current):
            counter +=1
            current = current.next
        return counter
        
        
    def isEmpty(self):
        return self.head == None
    
        
    def printelem(self):
        if self.head == None:
            return None
        else:
            current = self.head
            while (current):
                print(current.data)
                current = current.next
    

    def pushfront(self,elem):
            current = node(elem,self.head)
            self.head = current
            if self.tail == None:
                self.tail = self.head
    
    def topfront(self):
        return self.head
        
    
    def popfront(self):
        if self.head == None:
            self.tail = None
        else:
            current = self.head   
            self.head = current.next
          
    def pushback(self,elem):
        newnode = node(elem,none)
        if self.tail == None:
            self.tail = newnode
            self.head = self.tail
        else:
            self.tail.next = newnode
            self.tail = newnode
            
    def popback(self):
        if self.head == None:
            return 
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while (current.next.next):
                current = current.next
            current.next = None
            self.tail = current
            
            