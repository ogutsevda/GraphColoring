import numpy as np


def generate_graph_adj(n):
    adj = np.random.random((n, n)) < 0.5
    for i in range(adj.shape[0]):
        adj[i, i] = False
        for j in range(i + 1, adj.shape[1]):
            adj[i, j] = adj[j, i]

    return adj