import utils
import numpy as np


def two_opt_func(num, points, init_order, dist_matrix):
    tour_init = points[init_order]
    new_order = init_order.copy()
    improved = True
    replace = 0
    while improved:
        improved = False
        for i in range(1, num - 1):
            for j in range(i + 2, num + 1):
                if i == 1 and j == num:
                    continue
                t1, h1 = new_order[i - 1], new_order[i]
                t2, h2 = new_order[j - 1], new_order[j % num]
                change = dist_matrix[t2, t1] + dist_matrix[h2, h1] - dist_matrix[h1, t1] - dist_matrix[h2, t2]
                if change < 0:
                    new_order[i:j] = new_order[j - 1:i - 1:-1]
                    improved = True
                    replace += 1
    tour = np.array([points[new_order[i]] for i in range(num)])
    return new_order, tour_init, tour, replace


if __name__ == '__main__':
    number_points = 30
    rng = np.random.default_rng(4)
    data = rng.random((number_points, 2))
    # data = np.array([[0, 0.5], [0, 1], [1, 1.5], [2, 1.5], [4, 0], [5, 0],
    #                  [6, 0.5], [6, 1], [5, 1.5], [4, 1.5], [2, 0], [1, 0]])

    order, matrix = utils.initial_tour(number_points, data, False, 0)
    _, init_tour, two_opt_tour, _ = two_opt_func(number_points, data, order, matrix)

    print(f'Initial tour length: {utils.tour_length(init_tour)}'
          f'\n2-opt tour length: {utils.tour_length(two_opt_tour)}')
    utils.show_tour(init_tour, two_opt_tour)
