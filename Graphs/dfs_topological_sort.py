class topology_dfs():

    def __init__(self):
        self.vertices=6
        self.stack=[]
        self.visited={}
        self.graph = {"A": ["D", "C", "B"],
                     "B": ["E"],
                     "C": ["G", "F"],
                     "D": ["H"],
                     "E": ["I"],
                     "F": ["J"]}

    def _topological_sort(self, vertex):

        self.visited[vertex]=True

        if vertex in self.graph:
            for nodes in self.graph[vertex]:


                if nodes not in self.visited:
                    self._topological_sort(nodes)

        self.stack.append(vertex)

    def topological_sort(self):

        for vertex in self.graph.keys():

            if vertex not in self.visited:
                self._topological_sort(vertex)

        print(self.stack)

topology_dfs().topological_sort()
