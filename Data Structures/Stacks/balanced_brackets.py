#!/bin/python3

import sys

class stack(object):
    def __init__(self):
        self.data = []
        
    def push(self,val):
        self.data.append(val)
        
    def pop(self):
        self.data.pop()
        
    def peek(self):
        return self.data[-1]
    
    def isEmpty(self):
        return self.data == []
    
    
    
def isBalanced(s):
    pardict = ['{','[','(']
    st = stack()
    for i in s:
        if i in pardict:
            st.push(i)
        elif st.isEmpty() == False :
            if (i == '}' and st.peek() == '{') or (i == ']' and st.peek() == '[') or (i == ')' and st.peek() == '('):
                st.pop()
            else:
                return False
        else:
            return False
    return st.isEmpty()   
    
    
    

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        result = isBalanced(s)
        if result == True:
            print('YES')
        else:
            print('NO')
