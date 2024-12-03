from WeightedGraph import *
from Dijkstra import *

# main to test cases
    # this example uses a graph based off real routes from a house to a grocery store
    # the weights are based on distance in miles. It is a small graph where the vertices are close to each other so the weights are small
    # you can create your own graph and assign desired weights that correspond to the distance, you can also include a speed limit and traffic rate to see if the paths change
if __name__ == "__main__":
    # test with small graph that represents real-world data of routes from home to walmart
    # create graph to test;
    testGraph = WeightedGraph(14)  #vertex 0 is home and vertex 13 is walmart

    # add route 1 (should be faster route according to GPS)
    testGraph.add_edge(0, 1, .1, 25) # go to nearest intersection to home
    testGraph.add_edge(1, 2, .03, 25)
    testGraph.add_edge(2, 3, .09, 35)
    testGraph.add_edge(3, 4, .1, 35, "light")
    testGraph.add_edge(4, 5, .1, 35, "light")
    testGraph.add_edge(5, 6, .1, 35, "light")
    testGraph.add_edge(6, 13, .08, 5) # connect walmart to nearest intersection of route 1

    # add edges between routes
    testGraph.add_edge(2, 9, .2, 35)
    testGraph.add_edge(4, 10, .3, 30)
    testGraph.add_edge(5, 11, .3, 35,"moderate")

    # add route 2 (neighborhood route)
    testGraph.add_edge(0, 7, .1, 25) # go opposite from route 1 and to the nearest intersection to home
    testGraph.add_edge(7, 8, .05, 25)
    testGraph.add_edge(8, 9, .1, 25)
    testGraph.add_edge(9, 10, .1, 35)
    testGraph.add_edge(10, 11, .2, 35)
    testGraph.add_edge(11, 12, .07, 35)
    testGraph.add_edge(12, 13, .1, 10)  # connect walmart to nearest intersection of route 2


    start_vertex = 0 # home vertex
    end_vertex = 13 # walmart vertex
    print("\nShortest paths: ")
    classDistance, classPath = Dijkstra(testGraph, start_vertex) # call algorithm and start at home vertex
    printSolution(start_vertex, classDistance, classPath) # print all minimum-weight paths
    getXYPath(start_vertex, end_vertex, classPath) # print the shortest path from home to walmart

    #fastest route was route 1!