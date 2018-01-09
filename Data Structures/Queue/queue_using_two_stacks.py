class stack(object):
    def __init__(self):
        self.data = []
        
    def push(self, val):
        self.data.append(val)
        
    def pop(self):
        self.data.pop()
        
    def peek(self):
        return self.data[-1]
    
    def isEmpty(self):
        return self.data == []
    
    def getelem(self):
        return self.data
    
    
num = int(input())
st = stack()
stOpt = stack()


for i in range(num):
    elem = list(map(int,input().strip().split(' ')))
    if elem[0] == 1:
        st.push(elem[1])
    elif elem[0] == 2:        
        if stOpt.isEmpty():
            while st.isEmpty() == False:
                stOpt.push(st.peek())
                st.pop()
            stOpt.pop()
        else:
            stOpt.pop()     
    else:
        if stOpt.isEmpty():
            while st.isEmpty() == False:
                stOpt.push(st.peek())
                st.pop()
            print(stOpt.peek())
        else:
            print(stOpt.peek())
        
       