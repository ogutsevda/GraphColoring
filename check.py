
def color_check(adj_matrix, color_list, check_flag=False):
    for i in range(adj_matrix.shape[0]):
        for j in range(i + 1, adj_matrix.shape[1]):
            if adj_matrix[i, j]:
                if color_list[i] == color_list[j]:
                    check_flag = True
                    print('Invalid coloring!')
                    break
        if check_flag:
            break

    return check_flag
