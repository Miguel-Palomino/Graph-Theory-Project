from WeightedGraph import *
from Dijkstra import *

# main to test cases
    #this example compares the paths found between two similar graphs, one takes into account all factors (speed limit and traffic) and one doesn't
    #this example also uses an in-class example to ensure we get the same paths from the "root" to any other vertex
if __name__ == "__main__":
    # test graph with only distance weight
    test_graph = WeightedGraph(6)
    test_graph.add_edge(0,1, 4)
    test_graph.add_edge(0,5, 10)
    test_graph.add_edge(0,3, 3)
    test_graph.add_edge(1,2, 4)
    test_graph.add_edge(3,4, 2)
    test_graph.add_edge(4,5, 3)
    test_graph.add_edge(4,2, 2)

    #test graph using speedLimit and traffic factors that affect the weight
    test_graph2 = WeightedGraph(6)
    test_graph2.add_edge(0,1, 4, 10, "Light")
    test_graph2.add_edge(0,5, 10, 40) # no traffic
    test_graph2.add_edge(0,3, 3, 25,"moderate")
    test_graph2.add_edge(1,2, 4, 15,"moderate")
    test_graph2.add_edge(3,4, 2, 30 ,"heavy")
    test_graph2.add_edge(4,5, 3, 25,"light")
    test_graph2.add_edge(4,2, 2, 30,"heavy")

    start = 0
    end = 5
    # test_graph.print_graph() # print_graph shows adjacency matrix
    print("No factors included (only distance weight):")
    distance, path = Dijkstra(test_graph, start)
    printSolution(start, distance, path)
    getXYPath(start, end, path)
    print("\n")#add new line
    print("Factors included (speed limit and traffic):")
    # test_graph2.print_graph() # print adjacency matrix for test_graph2
    distance2, path2 = Dijkstra(test_graph2, start)
    printSolution(start, distance2, path2)
    getXYPath(start, end, path2)

    #test with example given in class
    testGraph = WeightedGraph(9)
    testGraph.add_edge(0, 1, 4)
    testGraph.add_edge(0, 7, 8)
    testGraph.add_edge(1, 7, 11)
    testGraph.add_edge(1, 2, 8)
    testGraph.add_edge(2, 3, 7)
    testGraph.add_edge(2, 8, 2)
    testGraph.add_edge(2, 5, 4)
    testGraph.add_edge(7, 8, 7)
    testGraph.add_edge(7, 6, 1)
    testGraph.add_edge(6, 8, 6)
    testGraph.add_edge(6, 5, 2)
    testGraph.add_edge(5, 3, 14)
    testGraph.add_edge(5, 4, 10)
    testGraph.add_edge(3, 4, 9)
    print("\n\nIn-class example paths:")
    classDistance, classPath = Dijkstra(testGraph, start)
    printSolution(start, classDistance, classPath)
