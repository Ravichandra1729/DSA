class Node:
    def __init__(self,Data):
        self.Data=Data
        self.next=None 
class LinkedList:
    def __init__(self,head):
        self.head=None
        self.next=None
    def add(self,value):
        if self.head is None