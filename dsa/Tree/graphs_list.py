def add_nodes(v):
    if v in graph:
        print(v,"is already present in graph")
    else:
        graph[v]=[]
def add_edge(v1,v2,cost):
    if v1 not in graph:
        print(v1, "is not present")
    elif(v2 not in graph):
        print(v2,"is not present")
    else:
        list1=[v2,cost]
        list2=[v1,cost]
        graph[v1].append(list1)
        graph[v2].append(list2)

def delete_node(v):
    if v not in graph:
        print(v ,"is not present")
    else:
        graph.pop(v)
        for i in graph:
            list1=graph[i]
            # if v in list1:
                # list1.remove(v)
            for j in list1:
                if v==j[0]:
                    list1.remove(j)
                    break
def delete_edge(v1,v2,cost):
    if v1 not in graph:
        print(v1, "is not present")
    elif(v2 not in graph):
        print(v2,"is not present")
    else:
        temp=[v1,cost]
        temp1=[v2,cost]
    
        # if v2 in graph[v1]:
            # graph[v1].remove(v2)
            # graph[v2].remove(v1)
        if temp1 in graph[v1]:
            graph[v1].remove(temp1)
            graph[v2].remove(temp)
graph={}
add_nodes("A")
add_nodes("B")
add_nodes("C")
print(graph)
add_edge("A","C",20)
print("after adding edge",graph)
delete_edge("A","C",20)
print(graph)
