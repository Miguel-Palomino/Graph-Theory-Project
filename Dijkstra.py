from WeightedGraph import *
import heapq
import math

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

def Dijkstra(g, start): #dijkstra's algorithm will find the minimum-weight path from the start vertex to any other vertex
    #root = 0  # assign vertex 0 as the root/source
    Visited = [False] * g.num_nodes # visited set; no vertices have been visited yet
    distance = [math.inf] * g.num_nodes # vertex cost, set all vertices cost to infinity
    path = [-1] * g.num_nodes # tree
    distance[start] = 0  # distance to root is 0
    pq = [] #initilize empty priority queue
    heapq.heappush(pq, (0, start)) # insert the first item to priority queue
    # See here https://docs.python.org/3/library/heapq.html for more information about heapq.
    while pq:
        cost, u = heapq.heappop(pq) #heappop pops and returns smallest item from the heap; smallest element is always at the root
            #cost will be assigned the value that is first in the paranthesis and u will be assigned the vertex associated with that cost
        # if u == end:
        #     break
        if Visited[u]: #if the vertex is visited then don't proceed with the algorithm and move on to a different vertex
            continue
        Visited[u] = True #if vertex was not visited, now visit it and do algorithm
        #to check for neighbors check the row of the vertex and find a nonzero value
        for v, w in enumerate(g.adj_matrix[u]): #v will hold the vertex adjacent to u and w will hold the weight of the edge conecting those vertices
            if not Visited[v] and w > 0: #if v is not visited and w of vertex is less than the cost already signed to and it is a nonzero value
                newCost = cost + w
                if newCost < distance[v]:
                    distance[v] = newCost
                    path[v] = u
                    heapq.heappush(pq, (newCost, v)) #push new value into priority queue (pq, (cost, vertex))
    printSolution(start, distance, path)
    # return distance[end], path #return distance and shortest path to any vertex

#Source for these print functions is https://www.geeksforgeeks.org/printing-paths-dijkstras-shortest-path-algorithm/
def printSolution(start, distance, path):
    vertices = len(distance)
    print("Vertex\t  Distance\t  Path")

    for vertex_index in range(vertices):
        if vertex_index != start:
            print("\n", start, "->", vertex_index, "\t\t", distance[vertex_index], "\t\t", end="")
            printPath(vertex_index, path)
def printPath(current, path):
    if current == -1:
        return
    printPath(path[current], path)
    print(current, end=" ")

# test
test_graph = WeightedGraph(5)
test_graph.add_edge(0,3, 2)
test_graph.add_edge(0,2, 4)
test_graph.add_edge(1,3, 6)
test_graph.add_edge(1,2, 1)
test_graph.add_edge(2,3, 3)
test_graph.add_edge(2,4, 10)
test_graph.add_edge(3,4, 5)

# test_graph.print_graph()
start = 0
end = 2
Dijkstra(test_graph, start)
