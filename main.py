import numpy as np
import matplotlib.pyplot as plt
import generate, algo, visu, check

repeat = 100
color_list = ["gold", "violet", "limegreen", "red", "darkorange"]
              #"yellow", "green", "black", "white", "pink"]
k = len(color_list)
incorrect = 0
nodes = np.arange(1, 26)
success_perc = np.zeros(25)

# visu.draw_graph_from_adjacency(adj, colors)

for n in nodes:
    for i in range(repeat):
        np.random.seed()
        adj = generate.generate_graph_adj(n)
        colors = algo.k_colorable(adj, color_list)
        check_flag = check.color_check(adj, colors, check_flag=False)
        # visu.draw_graph_from_adjacency(adj, colors)
        if check_flag:
            incorrect += 1

    success_perc[n-1] = repeat - incorrect
    incorrect = 0

print(success_perc)
plt.plot(nodes, success_perc)
plt.xlabel('Number of Nodes (n)')
plt.ylabel('Success Percentage')
plt.title(f'Percentage of Successful Colorings vs Number of Nodes with k={k}')
#plt.xticks(np.arange(1, 26, step=3))
plt.grid()
plt.show()
