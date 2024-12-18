import heapq
import math

def Dijkstra(g, start): #dijkstra's algorithm will find the minimum-weight path from the start vertex to any other vertex
    #root = 0  # assign vertex 0 as the root/source
    Visited = [False] * g.num_nodes # visited set; no vertices have been visited yet
    distance = [math.inf] * g.num_nodes # vertex cost, set all vertices cost to infinity
    path = [-1] * g.num_nodes # tree
    distance[start] = 0  # distance to root is 0
    pq = [] #initilize empty priority queue
    heapq.heappush(pq, (0, start)) # insert the first item to priority queue; heapq is automatically sorted, the smallest weight is at index-0
    # See here https://docs.python.org/3/library/heapq.html for more information about heapq.
    while pq:
        cost, u = heapq.heappop(pq) #heappop pops and returns smallest item from the heap; smallest element is always at the root
            #cost will be assigned the value that is first in the parenthesis and u will be assigned the vertex associated with that cost
        if Visited[u]: #if the vertex is visited then don't proceed with the algorithm and move on to a different vertex
            continue
        Visited[u] = True #if vertex was not visited, now visit it and do algorithm
        #to check for neighbors check the row of the vertex and find a nonzero value
        for v, w in enumerate(g.adj_matrix[u]): #v will hold the vertex adjacent to u and w will hold the weight of the edge connecting those vertices
            if not Visited[v] and w > 0: #if v is not visited and w of vertex is less than the cost already signed to, and it is a nonzero value
                newCost = cost + w
                if newCost < distance[v]:
                    distance[v] = newCost
                    path[v] = u
                    heapq.heappush(pq, (newCost, v)) #push new value into priority queue (pq, (cost, vertex))
    # printSolution(start, distance, path)
    return distance, path #return distance and shortest path to any vertex

#Source for these print functions is https://www.geeksforgeeks.org/printing-paths-dijkstras-shortest-path-algorithm/
def printSolution(start, distance, path):
    vertices = len(distance)
    print(" Vertex\t    Cost\t      Path")

    for vertexIndex in range(vertices):
        if vertexIndex != start:
            print("\n", start, "->", vertexIndex, "\t", "{:.2f}".format(distance[vertexIndex]), "\t\t", end="") # "{:.2f}".format(x) makes all values show two decimals
            printPaths(vertexIndex, path)

def printPaths(current, path):
    if current == -1: # current will be -1 if there are no paths left
        return
    printPaths(path[current], path)
    print(current, end=" ")

def getXYPath(start, end, path):
    currentVertex = end
    route = []
    while currentVertex != -1:  # reconstruct path from end to start
        route.append(currentVertex) # add current vertex to the end of route list
        currentVertex = path[currentVertex] # add path that led to the end vertex
    if route[-1] != start:  # if the start node isn't in the path, no valid path exists
        print(f"No path exists from {start} to {end}")
        return
    route.reverse()  # reverse the path to get start -> end order
    print("\n")
    print(f"xy-path from {start} to {end} is: ")
    print(" -> ".join(map(str, route))) # join route vertex number into string and output final string combined

