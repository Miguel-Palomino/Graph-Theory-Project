This code needs all 3 .py files in the same directory to work.

This code is a small representation of how a GPS works.

In this code, the user is able to create a graph and add edges between any vertices in the graph
* In these graphs
  * Vertices = Location/intersection;
  * Edges = Roads connecting the intersections

This code uses **weighted** graphs
* The weight represents the cost of traversing a road/edge
  * Weight is determined by distance and it is affected by the speed limit and/or traffic
    * Speed limit (optional)
      * Speed limit must be anything greater than 0
        * As the speed limit increases, the weight decreases 
    * Traffic rate (optional)
      * As traffic increases, the weight increases as well 
      * Traffic rate options are:
        * "light"
          * 10% increase
        * "moderate"
          * 20% increase
        * "heavy"
          * 30% increase

This code uses Dijkstra's algorithm to find the minimum-weight path from a start vertex to any other vertex in the graph.
* After finding the path(s), it returns the distance list and path list
  * Distance list holds all distances from the start vertex to any other vertex in the graph
  * path list holds all paths from start vertex to any other vertex in the graph

The main.py file is where we test cases (an example is provided in main.py)
* Our main.py compares the graph with only distance weights against a graph with all factors included
* To create a graph we call WeightedGraph(x), i.e. variable = WeightedGraph(x)
  * this creates an empty graph of x vertices
  * vertex indexing is 0-index based (from 0 to x-1), so vertex 1 would correspond 0 and vertex 6 would correspond to 5
* Next, call add_edge(node1, node2, weight, speedLimit (optional), traffic (optional))
  * i.e. variable.add_edge(...) 
  * This adds an edge between node1 and node2 with the given weight
    * User assigns desired initial weight based on the distance
    * If speedLimit and traffic are not given, it will assign the given weight directly to that edge
    * If speedLimit and/or traffic are given, the code will adjust the given weight accordingly
* After creating the graph with the desired edges and weights, we can call Dijkstra's algorithm (Dijkstar(graph, start_vertex))
  * i.e: distance, path = Dijkstra(variable, start_vertex)
    * distance will hold the distance list returned by the algorithm
    * path will hold the path list returned by the algorithm
*  Finally, we can either call printSolution(start_vertex, distance, path) or getXYPath(start_vertex, end_vertex, path)
   * printSolution(start_vertex, distance, path) will print **ALL** minimum-weight paths found in the graph
     * start_vertex is the node we wish to start at
     * distance is the distance variable that holds the distance list returned from the algorithm
     * path is the path variable that holds the path list returned from the algorithm
   * getXYPath(start_vertex, end_vertex, path) returns **ONLY** the minimum-weight path from start_vertex to end_vertex
     * start_vertex is the node we wish to start at
     * end_vertex is the node we wish to end at
     * path is the path variable that holds the path list returned from the algorithm

This is not the full representation how a GPS finds routs, but rather how Dijkstra's algorith is used, thank you!
