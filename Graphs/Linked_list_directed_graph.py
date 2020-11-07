#Python Code to implement Linked list representation of directed Graph


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class Graph:

    def __init__(self, size):
        self.size = size
        self.graph_array = [None for _ in range(self.size)]

    def find_node(self, key):

        if self.graph_array[key] is None:
            return 0
        else:
            return 1

    def add_edge(self, source, destination):

        #print("source-dest", source,destination)
        exists = self.find_node(source)
        if exists == 1:
            head = self.graph_array[source]
            while head.next is not None:
                head = head.next
            head.next = Node(destination)
            #print("Added edge between", source, destination)

        else:
            self.graph_array[source] = Node(destination)
            #print("Added edge between", source, destination)

    def print_graph(self):
        for i in range(self.size):
            print(i,"->",end="")
            temp=self.graph_array[i]
            while temp is not None:
                print(temp.val,"->",end=" ")
                temp=temp.next
            print("None")
            print("\n")


if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()

