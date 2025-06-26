import utils
import numpy as np
import time


def two_opt_func2(num, points, init_order, dist_matrix):
    tour_init = np.array([points[init_order[i]] for i in range(num)])
    new_order = init_order
    improved = True
    indices = [set(np.where(row < 2)[0]) for row in dist_matrix]
    while improved:
        improved = False
        for i in range(1, num - 1):
            b = i
            best_change = 0
            for j in range(i + 2, num + 1):
                if i == 1 and j == num:
                    continue
                t1, h1 = new_order[i - 1], new_order[i]
                t2, h2 = new_order[j - 1], new_order[j % num]
                if t2 in indices[t1] or h2 in indices[h1]:
                    change = dist_matrix[t2, t1] + dist_matrix[h2, h1] - dist_matrix[h1, t1] - dist_matrix[h2, t2]
                    if change < best_change:
                        best_change = change
                        b = j
            if best_change < 0:
                new_order[i:b] = new_order[b - 1:i - 1:-1]
                improved = True
    tour = np.array([points[new_order[i]] for i in range(num)])
    return new_order, tour_init, tour


if __name__ == '__main__':
    number_points = 30
    rng = np.random.default_rng(2)
    data = rng.random((number_points, 2))

    start1 = time.time()
    order, matrix = utils.initial_tour(number_points, data, False, 0)
    _, init_tour, two_opt_tour = two_opt_func2(number_points, data, order, matrix)
    end1 = time.time()
    print(f'Running time: {end1 - start1}')

    print(f'Construction tour length: {utils.tour_length(init_tour)}'
          f'\n2-opt tour length: {utils.tour_length(two_opt_tour)}')
    # utils.show_tour(init_tour, two_opt_tour)
