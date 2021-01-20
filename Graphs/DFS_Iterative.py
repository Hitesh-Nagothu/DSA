"""
*******************ITERATIVE DFS APPROACH************************

stack=[]
visited=[]

DFS(source):
    1. Append source to stack
    2. Append source to visited array

    while stack is not empty:
        s=stack.pop()

        if s not in visited:
            visited.append(s)


        for each neighbour of s:
            stack.append(neighbour)




"""

graph = {"A":["D","C","B"],
   "B":["E"],
   "C":["G","F"],
   "D":["H"],
   "E":["I"],
   "F":["J"]}

stack=[]
visited=[]

def DFS(source):
    stack.append(source)  #Push to stack

    while len(stack)!=0:
        s=stack.pop()

        if s not in visited:
            visited.append(s)

        if s not in graph:
            continue

        for node in graph[s]:
            stack.append(node)

    return " ".join(visited)

print(DFS("A"))

