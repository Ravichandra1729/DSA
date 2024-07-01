print("queue")
#follows first in first out 


#using list 
queue0=[]
def enqueue(element):
    queue0.append(element)
def dequeue():
    queue0.pop(0)
enqueue(22)
enqueue(44)
enqueue(55)
dequeue()
dequeue()
print(queue0)

#anothe way 
queue1=[]
queue1.insert(0,10)
queue1.insert(0,20)
queue1.insert(0,30)
queue1.insert(0,40)
queue1.pop()
print(queue1)




#using classess
#double ended-queue  from collections
import collections
queue2=collections.deque()
queue2.append(20)
queue2.append(30)
queue2.append(49)
queue2.popleft()
print(queue2)
#Note:I can also use appendleft and pop

#priority Queue
#using list we can implement
queue4=[]
queue4.append(10)
queue4.sort()
queue4.append(150)
queue4.sort()
queue4.append(130)
queue4.sort()
queue4.append(130)
queue4.sort()
queue4.pop(0)
print(queue4)
#using priority Queue
import queue

q=queue.PriorityQueue()
q.put(10)
q.put(60)
q.put(20)
q.put(40)
q.put(40)
print("priority queu",q)
q.get()
print("priority queue",q)








#using queue
import queue
queue3=queue.Queue()
queue3.put(10)
queue3.put(50)
queue3.put(70)
queue3.get()
print(queue3)

