import numpy as np


def k_colorable(adj_matrix, color_list):
    flag = False
    k = len(color_list)
    indexes = [i for i in range(k)]
    temp_color_list = [indexes[0]] * adj_matrix.shape[0]
    for i in range(adj_matrix.shape[0]):
        for j in range(i + 1, adj_matrix.shape[1]):
            if adj_matrix[i, j]:
                if temp_color_list[i] == temp_color_list[j]:
                    connected = [l for l in np.where(adj_matrix[j, :])[0]]
                    neighbor_colors = [temp_color_list[r] for r in connected]
                    diff = set(indexes) - set(neighbor_colors)
                    if diff:
                        new_color = min(diff)
                        temp_color_list[j] = new_color
                    else:
                        flag = True
                        print(f'This graph is not k-colorable where k={k}!')
                        break
        if flag:
            break

    graph_coloring = [color_list[m] for m in temp_color_list]

    return graph_coloring
