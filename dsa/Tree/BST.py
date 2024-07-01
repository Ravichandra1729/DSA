#Implementation of binary Tree

class BST:
    def __init__(self,key):
        self.key=key 
        self.lchild=None 
        self.rchild=None 
    def insert(self,data):
        if self.key is None:
            self.key=data
            return 
        if self.key==data:
            return 
        if(self.key>data):
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
    def search(self,data):
        if self.key ==data:
            print('Node is found')
            return 
        if data<self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print('Node is not found')
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print('Node is not present')
    def preorder(self):
        print(self.key,end=' ')
        if(self.lchild):
            self.lchild.preorder()
        if(self.rchild):
            self.rchild.preorder()
            
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=' ')
        if self.rchild:
            self.rchild.inorder()
    def postorder(self):
        if self.lchild:
            self.lchild.inorder()
        if self.rchild:
            self.rchild.inorder()
        print(self.key,end=' ')
    def delete(self,data,curr):
        if self.key is None:
            print('Tree is EMpty')
            return 
        if data<self.key:
            if self.lchild:
                self.lchild=self.lchild.delete(data,curr)
            else:
                print('given Node is not present')
        elif(data>self.key):
            if self.rchild:
                self.rchild=self.rchild.delete(data,curr)
            else:
                print('given Node is not present')
        else:
            if self.lchild is None:
                temp=self.rchild
                if data==curr:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                if data==curr:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return
                self=None
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(node.key,curr)
        return self
        
        
    def min_node(self):
        cuurent=self
        while cuurent.lchild:
            cuurent=cuurent.lchild
        print("node with smallest key is :",cuurent.key)
    def max_node(self):
        cuurent=self
        while cuurent.rchild:
            cuurent=cuurent.rchild
        print("node with maximum key is :",cuurent.key)
def count(node):
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild)
            
root=BST(10)
list1=[6,3,1,6,98,3,7]
for i in list1:
    root.insert(i)
root.search(11)
print("count",count(root))
print("preorder")
root.preorder()
print('Inorder')
root.inorder()
print("postorder")
root.postorder()
if count(root)>1:
    root.delete(10,root.key)
else:
    print("Can't perform deletion operation")
print("after Deleting")
root.preorder()

root.min_node()
root.max_node()
# print(root.key)
# print(root.lchild)
# print(root.rchild)
