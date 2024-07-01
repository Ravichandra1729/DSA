def add_nodes(v):
    if v in graph:
        print(v,"is already present in graph")
    else:
        graph[v]=[]
def add_edge(v1,v2):
    if v1 not in graph:
        print(v1, "is not present")
    elif(v2 not in graph):
        print(v2,"is not present")
    else:
        #list1=[v2,cost]
        #list2=[v1,cost]
        graph[v1].append(v2)
        graph[v2].append(v1)
#recurssive
def DFS(node,visited,graph):
    if node not in graph:
        print("Node is not present")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)
def DFS_IT(node,graph):
    visitedIt=set()
    if node not in graph:
        print("Node is not present")
        return
    stack=[]
    stack.append(node)
    while stack:
        current=stack.pop()
        if current not in visitedIt:
            visitedIt.add(current)
            print(current)
            for i in graph[current]:
                stack.append(i)
visited=set()   
graph={}
add_nodes("A")
add_nodes("B")
add_nodes("C")
add_nodes("D")
add_nodes("E")
add_edge("A","B")
add_edge("B","E")
add_edge("A","C")
add_edge("A","D")
add_edge("B","D")
add_edge("C","D")
add_edge("E","D")
print(graph)
#DFS("A",visited,graph)
DFS_IT("A",graph)