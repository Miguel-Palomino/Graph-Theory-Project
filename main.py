from WeightedGraph import *
from Dijkstra import *

# main to test cases
if __name__ == "__main__":
    # test
    test_graph = WeightedGraph(6)
    test_graph.add_edge(0,1, 6, 10, "light")
    test_graph.add_edge(0,5, 7, 5,"moderate")
    test_graph.add_edge(4,5, 4, 25,"light")
    test_graph.add_edge(4,2, 4, 30,"high")
    test_graph.add_edge(2,3,7, 15,"heavy")

    start = 0

    Dijkstra(test_graph, start)





