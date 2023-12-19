import networkx as nx
import matplotlib.pyplot as plt


class GraphVisualization:

    def __init__(self):
        # visual is a list which stores all
        # the set of edges that constitutes a
        # graph
        self.edges = []
        self.node_color = None

    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def addEdge(self, a, b):
        temp = [a, b]
        self.edges.append(temp)

    def setColors(self, colors):
        self.node_color = colors

    # in visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.edges)
        print(self.node_color)
        nx.draw_networkx(G, nodelist=[i for i in range(len(self.node_color))], node_color=self.node_color,
                         with_labels=True)
        plt.show()


def draw_graph_from_adjacency(adj, colors):
    GV = GraphVisualization()
    for i in range(adj.shape[0]):
        for j in range(i + 1):
            if adj[i, j]:
                GV.addEdge(i, j)

    GV.setColors(colors)
    GV.visualize()
