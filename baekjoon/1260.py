import sys

def dfs(graph, start_node, visited=list()):
    visited.append(start_node)
    print(start_node, end=" ")
    for node in graph[start_node]:
       if node not in visited:
           dfs(graph,node,visited)

def bfs(graph, start_node,visited = list()):
    queue = list()
    queue.append(start_node)
    while queue:
         node = queue.pop(0)
         if node not in visited:
              visited.append(node)
              print(node, end=" ")
              queue.extend(graph[node])
   
              
N,M,V = map(int,sys.stdin.readline().split())
graph = {}
for i in range(0,M):
    A,B = map(int,sys.stdin.readline().strip().split())
    if A in graph:
        graph[A].append(B)
    else:
        graph[A] = [B]
    if B in graph:
        graph[B].append(A)
    else:
        graph[B] = [A]
for value in graph.values():
    value.sort()
print(graph)
dfs(graph, V)
print()
bfs(graph, V)