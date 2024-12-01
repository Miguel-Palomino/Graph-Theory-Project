import math

class WeightedGraph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        # Initialize a 2D matrix with zeros
        self.adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    def add_edge(self, node1, node2, weight, speedLimit, traffic = None):
        #initial weight is user-decided based on distance, the speedLimit will reduce the weight, and the traffic will increase it
        weight += .0 * weight #just preference to make all weights float when displaying
        if speedLimit <= 0:
            print("Error: speed limit must be a positive integer \n")
        elif speedLimit >= 0 and speedLimit <= 10:
            weight = weight - (.05 * weight)
        elif speedLimit > 10  and speedLimit <= 20:
            weight = weight - (.10 * weight)
        elif speedLimit >= 0 and speedLimit <= 30:
            weight = weight - (.15 * weight)
        elif speedLimit >= 0 and speedLimit <= 40:
            weight = weight - (.20 * weight)
        elif speedLimit >= 0 and speedLimit <= 50:
            weight = weight - (.25 * weight)
        elif speedLimit >= 0 and speedLimit <= 60:
            weight = weight - (.35 * weight)
        elif speedLimit >= 0 and speedLimit <= 70:
            weight = weight - (.40 * weight)
        else:
            weight = weight - (.50 * weight)
        if traffic != None:
            if traffic == "light":
                weight += .1 * weight
            elif traffic == "moderate":
                weight += .2 * weight
            else: # if heavy traffic
                weight += .3 * weight
        self.adj_matrix[node1][node2] = weight
        self.adj_matrix[node2][node1] = weight

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
            print(" ".join(f"{w:.2f}" for w in row))
            #print(" ".join(map(str, row)))

if __name__ == "__main__":
    # use case
    test_graph = WeightedGraph(3)
    test_graph.add_edge(1,0, 2)
    test_graph.add_edge(1, 2, 3)
    test_graph.print_graph()
    print(test_graph.num_edges())
    print("\n")
    test_graph.print_graph()