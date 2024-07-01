print('stacks')

#using list:
stack=[]
def push(element):
    stack.append(element)
def pop():
    stack.pop()
push(10)
push(20)
push(30)
pop()
print(stack)

#using collections 
import collections
stack1=collections.deque()
stack1.append(22)
stack1.append(33)
stack1.append(55)
stack1.pop()
print(stack1)

#using queue
import queue
stack2=queue.LifoQueue()
stack2.put(44)
stack2.put(454)
stack2.put(444)
stack2.get()
print(stack2.queue)