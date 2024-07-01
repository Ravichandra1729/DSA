class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinekdList:
    def __init__(self):
        self.head=None
    def print_ll(self):
        if self.head is None:
            print('empty linkedList')
        else:
            n=self.head
            while n is not None:
                print(n.data,'--->',end=" ")
                n=n.ref
    def addBegin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
        
    def add_after_node(self,data,x):
        new_node=Node(data)
        n=self.head
        while n is not None:
            if n.data==x:
                break 
            n=n.ref
        if n is None:
            print('Node is not present in linkedList')
        else:
            new_node.ref=n.ref 
            n.ref=new_node
    def add_befor_node(self,data,x):
        if self.head is None:
            print('LinekdList is empty...!')
            return
        if self.head.data==x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return 
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break 
            n=n.ref 
        if n.ref is None:
            print('Node is not found..!')
        else:
            new_node=Node(data)
            new_node.ref=n.ref 
            n.ref=new_node
    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print('linekdlist is not empty')
    def delete_begin(self):
        
        if self.head is None:
            print('linekdlist is empty')
        else:
            self.head=self.head.ref
        
    def delete_from_end(self):
        if self.head is None:
            print('LinekdList is empty')
        elif(self.head.ref is None):
            self.head=None
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref 
            n.ref=None
    def delete_in_between(self,x):
        if self.head is None:
            print('LinekdList is empty')
            return 
        n=self.head
        if n.data==x:
            self.head=self.head.ref 
            return 
        
        while n.ref is not None:
            if(n.ref.data==x):
                break
            n=n.ref
        if n.ref is None:
            print('Node is not present')
        else:
            n.ref=n.ref.ref 
                
        
                
ll1=LinekdList()
ll1.addBegin(2)
ll1.addBegin(10)
ll1.add_at_end(22)
ll1.addBegin(9)
ll1.add_at_end(52)
ll1.add_at_end(32)
ll1.addBegin(1)
ll1.print_ll()
ll1.add_befor_node(1212,2)

ll1.add_after_node(1,111)
ll1.print_ll()
ll1.delete_begin()
ll1.delete_begin()
ll1.delete_from_end()
print('1\n')
ll1.print_ll()
ll1.delete_in_between(2)
print('XX','\n')
ll1.print_ll()