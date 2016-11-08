class Stack:
    def __init__(self):
        self.items = [0]
        self.size = 0
    
    def push(self,data):
        self.items.append(data)
        self.size+=1
    
    def pop(self):
        self.size-=1
        return self.items.pop()
    
    def peek(self):
        return self.items[self.size]
    
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class StackNode:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def push(self,data):
        node = Node(data)
        if self.head!=None:
            self.head.next = node
        self.head = node
        self.size+=1
        
    def pop(self):
        if self.head==None:
            print 'Stack empty'
            return
        else:
            data = self.head.data
            self.head = self.head.next
            self.size-=1
            return data
    
    def peek(self):
        if self.head==None:
            print 'Stack empty'
            return
        else:
            return self.head.data
        
        
            
    
    
        
            
        