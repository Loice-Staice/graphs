import matplotlib.pyplot as plt

# //line Graph
x_values = [1, 2, 3, 4]
y_values = [1, 4, 9, 16]


plt.plot(x_values, y_values)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.grid(True)  
plt.show()

# //undirected  graph
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def print_graph(self):
        for node in self.graph:
            print(f"{node} -> {', '.join(map(str, self.graph[node]))}")

my_graph = Graph()
my_graph.add_edge(1, 2)
my_graph.add_edge(1, 3)
my_graph.add_edge(2, 3)
my_graph.add_edge(3, 4)

my_graph.print_graph()


# //3 directed graph     edges have  directions
import matplotlib.pyplot as plt


x = [1, 2, 3]
y = [2, 4, 1]


plt.plot(x, y)


plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Complete graph')

plt.show()

# //4

class Graph:
    def __init__(self, size):
        self.adj_matrix = [[None] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(lambda x: str(x) if x is not None else '0', row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")
            
g = Graph(4)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_edge(0, 1, 3)
g.add_edge(0, 2, 2)
g.add_edge(3, 0, 4)
g.add_edge(2, 1, 1)
g.print_graph()


#
class Graph:
    def __init__(self, size):
     self.adj_matrix = [[0] * size for _ in range(size)]
     self.size = size
     self.vertex_data = [''] * size
    def add_edge(self, u, v):
     if 0 <= u < self.size and 0 <= v < self.size:
      self.adj_matrix[u][v] = 1
    def add_vertex_data(self, vertex, data):
     if 0 <= vertex < self.size:
      self.vertex_data[vertex] = data
    def print_graph(self):
     print("Adjacency Matrix:")
     for row in self.adj_matrix:
      print(' '.join(map(str, row)))
     print("\nVertex Data:")
     for vertex, data in enumerate(self.vertex_data):
      print(f"Vertex {vertex}: {data}")



