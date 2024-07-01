def add_node(v):
    global node_count
    if v in nodes:
        print(v,"node is already preset")
    else:
        node_count+=1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp=[]
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)
        
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j],"<3"),end=' ')
        print()
def add_edge(v1,v2,cost):
    if v1 not in nodes:
        print(v1,"is not preset")
    elif(v2 not in nodes):
        print(v2, "is not preset")
    else:
        index_v1=nodes.index(v1)
        index_v2=nodes.index(v2)
        graph[index_v1][index_v2]=cost
        graph[index_v2][index_v1]=cost
def delet_node(v):
    global node_count
    if v not in nodes:
        print(v," is not preset in the graph")
    else:
        index_v=nodes.index(v)
        node_count-=1
        nodes.remove(v)
        graph.pop(index_v)
        for i in graph:
            i.pop(index_v)
def delete_edge(v1,v2):
    if v1 not in nodes:
        print(v1," is not preset in the graph")
    elif v2 not in nodes:
        print(v2,"is not preset in the graph")
    else:
        index_v1=nodes.index(v1)
        index_v2=nodes.index(v2)
        graph[index_v1][index_v2]=0
        graph[index_v2][index_v1]=0
    
nodes=[]
graph=[]
node_count=0
#print("beofre adding nodes")
#print(nodes)
#print(graph)
add_node("A")
#print("after adding nodes")
#print(nodes)
#print(graph)
add_node("B")
#print("after adding nodes")
#print(nodes)
#print(graph)
add_node("C")
#print("after adding nodes")
#print(nodes)
#print(graph)
add_edge("A","B",10)
add_edge("A","C",5)
print("Before")
print_graph()
delete_edge("A","C")
print("after")
print_graph()
print(nodes)
