This code is a small representation of how a GPS works
In this code, the user is able to create a graph and add edges between any vertices in the graph
* In these graphs
  * Vertices = Location/intersection;
  * Edges = Roads connecting the intersections

This code uses Dijkstra's algorithm to find the minimum-weight path from a start vertex to any other vertex in the graph
* The weight represents the cost of traversing a road/edge
  * Weight is determined by distance and it is affected by the speed limit and/or traffic
    * Speed limit (optional)
      * Speed limit must be anything greater than 0
        * As the speed limit increases, the weight decreases 
    * Traffic rate (optional)
      * As traffic increases, the weight increases as well 
      * Traffic rate options are:
        * "light"
        * "moderate"
        * "heavy"
