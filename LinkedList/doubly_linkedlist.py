class Node:
    def __init__(self,data):
        self.data=data
        self.pref=None 
        self.nref=None
class doublyLinkedList:
    def __init__(self):
        self.head=None
    def print_ll(self):
        if self.head is None:
            print('Linked List is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data,'-->',end='')
                n=n.nref 
    def back_print_ll(self):
        if self.head is None:
            print('linkedlist isempty')
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,'-->',end='')
                n=n.pref
            
            
    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print('LinkedList is not Empty')
    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is None:
                n=n.nref
            n.nref=new_node
            new_node.pref=n
    def add_after(self,data,x):
        if self.head is None:
            print('LinkedList is empty ')
        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.nref 
            if n is None:
                print('Given Node is not present in doublyLinkedList')
            else:
                new_node=Node(data)
                new_node.nref=n.nref
                new_node.pref=n 
                if n.nref is not None:
                    n.nref.pref=new_node
                n.nref=new_node
                
    def add_before(self,data,x):
        if self.head is None:
            print('LinkedList is empty ')
        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.nref 
            if n is None:
                print('Given Node is not present in doublyLinkedList')
            else:
                new_node=Node(data)
                new_node.nref=n
                new_node.pref=n.pref
                if n.pref is not None:
                    n.pref.nref=new_node
                else:
                    self.head=new_node
                n.pref=new_node
    def delete_begin(self):
        if self.head is None:
            print('doublyLinkedList is empty')
            return 
        if self.head.nref is None:
            self.head=None
            print('DDL is empty after deleting this Node')
        else:
            self.head=self.head.nref 
            self.head.pref=None
    def delete_end(self):
        if self.head is None:
            print('doublyLinkedList is empty')
            return
        
        if self.head.nref is None: 
            self.head=None
            print('DDL is empty after deleting this Node')
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.pref.nref=None
            
    def delete_by_value(self,x):
        if self.head is None:
            print('doublyLinkedList is empty')
            return
        if self.head.nref is None:
            if self.head.data==x:
                self.head=None
            else:
                print("given node is not present in dd1") 
            return
        if self.head.data==x:
            self.head=self.head.nref
            self.head.pref=None
            return
        n=self.head
        while n.nref is not None:
            if n.data==x:
                break
            n=n.nref
        if n.nref is not None:
            n.pref.nref=n.nref
            n.nref.pref=n.pref
        else:
            if n.data==x:
                n.pref=None
            else:
                print("given Node is not present")
        
dd1=doublyLinkedList()
dd1.insert_empty(2)
dd1.add_begin(12)
dd1.add_begin(22)
dd1.add_after(4,22)
dd1.add_before(5,22)
#dd1.delete_begin()
dd1.delete_end()
dd1.print_ll()
dd1.delete_by_value(4)
print('\n')
dd1.back_print_ll()
