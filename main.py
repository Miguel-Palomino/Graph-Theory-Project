'''from WeightedGraph import *'''
import heapq
import math

class WeightedGraph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        # Initialize a 2D matrix with zeros
        self.adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    def add_edge(self, node1, node2, w):
        # TODO: Add an undirected edge between node1 and node2
        self.adj_matrix[node1][node2] = w
        self.adj_matrix[node2][node1] = w
        #pass #placeholder for empty function to get ignored

    def remove_edge(self, node1, node2):
        # Remove the edge between node1 and node2
        self.adj_matrix[node1][node2] = 0
        self.adj_matrix[node2][node1] = 0

    def num_edges(self):
        num_edges = 0
        for i in range(self.num_nodes):
            for j in range(i+1, self.num_nodes):
                if self.adj_matrix[i][j] != 0:
                    num_edges += 1
        return num_edges

    def print_graph(self):
        # Print the adjacency matrix
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))

# if __name__ == "__main__":
#     # use case
#     test_graph = WeightedGraph(3)
#     test_graph.add_edge(1,0, 2)
#     test_graph.add_edge(1, 2, 3)
#     test_graph.print_graph()
#     print(test_graph.num_edges())

def build_tree(T):
    """Builds a dictionary representing the tree from the list of parents."""
    n = len(T)
    tree = {i: [] for i in range(n)}  # Create an empty list for each node
    root = None

    # Construct the tree
    for child, parent in enumerate(T):
        if parent == -1:
            root = child  # Node with no parent is the root
        else:
            tree[parent].append(child)

    return tree, root

def print_tree(T):
    tree, root = build_tree(T)
    def print_tree(node, level=0):
        indent = "  " * level
        print(f"{indent}- Node {node}")
        for child in tree[node]:
            print_tree(child, level + 1)

    if root is not None:
        print_tree(root)
    else:
        print("No root found")

def Prim(g): #change this to Dijkstra's Algorithm

    root = 0  # assign vertex 0 as the root
    Visited = [False] * g.num_nodes # visited set
    T = [-1] * g.num_nodes # tree
    pq = []  # Priority queue to store vertices that are being processed
    c = [math.inf] * g.num_nodes # vertex cost
    c[0] = 0 # vertex cost of the root is 0
    heapq.heappush(pq, (0, root)) # insert the first item to priority queue

    # TODO: implement the while loop
    # See here https://docs.python.org/3/library/heapq.html for more information about heapq.
    while pq:
        cost, u = heapq.heappop(pq) #heappop pops and returns smallest item from the heap; smallest element is always at the root
            #cost will be assigned the value that is first in the paranthesis and u will be assigned the vertex associated with that cost
        if Visited[u]: #if the vertex is visited then don't proceed with the algorithm and move on to a different vertex
            continue
        Visited[u] = True #if vertex was not visited, now visit it and do algorithm
        #to check for neighbors check the row of the vertex and find a nonzero value
        for v, w in enumerate(g.adj_matrix[u]): #v will hold the vertex adjacent to u and w will hold the weight of the edge conecting those vertices
            if not Visited[v] and w < c[v] and w != 0: #if v is not visited and w of vertex is less than the cost already signed to and it is a nonzero value
                T[v] = u #update the parent of v
                c[v] = w #update cost of v
                heapq.heappush(pq, (w, v)) #push new value into priority queue (pq, (cost, vertex))
    return T #return minimum-weight spanning tree


# test
test_graph = WeightedGraph(5)
test_graph.add_edge(0,3, 2)
test_graph.add_edge(0,2, 4)
test_graph.add_edge(1,3, 6)
test_graph.add_edge(1,2, 1)
test_graph.add_edge(2,3, 3)
test_graph.add_edge(2,4, 10)
test_graph.add_edge(3,4, 5)
print_tree(Prim(test_graph))