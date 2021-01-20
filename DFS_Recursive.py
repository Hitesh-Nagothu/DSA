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
