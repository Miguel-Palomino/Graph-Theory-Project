from WeightedGraph import *
import heapq
import math

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
    print(" Vertex\t   Distance\t   Path")

    for vertexIndex in range(vertices):
        if vertexIndex != start:
            print("\n", start, "->", vertexIndex, "\t", round(distance[vertexIndex], 2), "\t\t", end="")
            printPaths(vertexIndex, path)
def printPaths(current, path):
    if current == -1:
        return
    printPaths(path[current], path)
    print(current, end=" ")

# test
test_graph = WeightedGraph(6)
test_graph.add_edge(0,1, 6, 10, "light")
test_graph.add_edge(0,5, 7, 5,"moderate")
test_graph.add_edge(4,5, 4, 25,"light")
test_graph.add_edge(4,2, 4, 30,"high")
test_graph.add_edge(2,3,7, 15,"heavy")

# test_graph.print_graph()
start = 0

Dijkstra(test_graph, start)
