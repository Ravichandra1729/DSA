#complete binary tree which satisfied the heap property
#heap property--key of a node is always greater or equal than its child node

#heapify-- it is a process to rearrange the elements of the heap in order to maintain the heap  property 
#heapify_up bottom-up during insertion we use this 
#heapify_down top-down durnig deletion we use this 
#list representiaon
#lchild=2*i+1
#rchild=2*i+2
#parent=(i-1)//2

import heapq
#syntax:heapq.heappush(heap,item)
heap=[]
heapq.heappush(heap,10)
heapq.heappush(heap,1)
heapq.heappush(heap,5)
print(heap)
heapq.heappop(heap)
print(heap)
#syntax:heapq.heapify(heap)

list1=[1,3,5,2,4,6]
heapq.heapify(list1)
print(list1)
#syntax:heapq.heappushpop(heap,item)perform push and pop minimum value 
heapq.heappushpop(list1,89)
print(list1)

#syntax:heapq.heapreplace(heap,item) pop smallest element and insert new element 
print(heapq.heapreplace(list1,100))
print(list1)
#syntax:heapq.nsmallest(n,iterable,key=None)gives n smallest number
heap1=[1,20,5,4,3,6,2]
print(heapq.nsmallest(2,heap1))
print(heapq.nlargest(2,heap1))

#priority queue

list2=[(1,'ria'),(4,'sia'),(3,'gia')]
for i in range(len(list2)):
    print(heapq.heappop(list2))


heapq.heapify(list2)
print(list2)

