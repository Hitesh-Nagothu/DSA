"""
*******************RECURSIVE DFS APPROACH************************

stack=[]
visited=[]

dfs(source, visited):
    1. If source not visited:
            #Add source to visited

            if source not in adjacency list or has no children:
                return visited

            for each neighbours of source:
                dfs(neighbour, visited)

        return visited

"""


graph = {"A": ["D", "C", "B"],
         "B": ["E"],
         "C": ["G", "F"],
         "D": ["H"],
         "E": ["I"],
         "F": ["J"]}


def dfs(source, visited=[]):
    if source not in visited:
        visited.append(source)

        if source not in graph:
            return visited

        for node in graph[source]:
            visited = dfs(node, visited)

    return visited


dfs_path = dfs("A")
print(" ".join(dfs_path))
