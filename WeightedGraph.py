import math

# R = 6371.0
# def haver_dist(lati1, long1, lati2, long2): #haversine function; The Haversine Formula is used to calculate the great-circle distance between two points on Earth given their latitude and longitude
#     lat1 = math.radians(lati1)          #haversine formula assumes earth is perfect sphere
#     lon1 = math.radians(long1)
#     lat2 = math.radians(lati2)
#     lon2 = math.radians(long2)
#     dlong = lon2 - lon1
#     dlati = lat2 - lat1
#     a = (
#             math.sin(dlati / 2) ** 2
#             + math.cos(lat1) * math.cos(lat2) * math.sin(dlong / 2) ** 2
#     )
#     c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
#     distance = R * c
#     return distance #distance given in kilometers

class WeightedGraph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        # Initialize a 2D matrix with zeros
        self.adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]
    #     self.coordinates = {}
    #
    # def add_node(self, node, lat, long):
    #     self.coordinates[node] = (lat, long)

    # def add_edge(self, node1, node2):
    #     lat1, long1 = self.coordinates[node1]
    #     lat2, long2 = self.coordinates[node2]
    #     weight = haver_dist(lat1, long1, lat2, long2)
    #     self.adj_matrix[node1][node2] = weight
    #     self.adj_matrix[node2][node1] = weight
    #     #pass #placeholder for empty function to get ignored

    def add_edge(self, node1, node2, w, directed = False):
        self.adj_matrix[node1][node2] = w
        if not directed:
            self.adj_matrix[node2][node1] = w

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