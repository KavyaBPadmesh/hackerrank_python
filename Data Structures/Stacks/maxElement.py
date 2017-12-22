num = int(input())

class stack(object):
    def __init__(self):
        self.data = [0]

    def push(self,val):
        self.data.append(max(val, self.data[-1]))
    
    def pop(self):
        self.data.pop()
    
    def printmax(self):
        print(self.data[-1])
        
        
dataary = stack()

for i in range(num):
    elem = list(map(int, input().split()))
    if elem[0] == 1:
        dataary.push(elem[1])
    elif elem[0] == 2:
        dataary.pop()
    else:
        dataary.printmax()
        