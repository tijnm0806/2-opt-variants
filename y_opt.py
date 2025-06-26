import utils
import numpy as np


def change_y_opt(tour, distances, num, p, q):
    t1, h1 = tour[p - 1], tour[p]
    t2, h2 = tour[q - 1], tour[q % num]
    e1, e2 = distances[h1, t1], distances[h2, t2]
    e3, e4 = distances[t2, t1], distances[h2, h1]
    if e1 + e2 > e3 + e4:
        if max(e1, e2) > max(e3, e4) and min(e1, e2) > min(e3, e4):
            return True
    return False


def y_opt_func(num, points, init_order, dist_matrix):
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
                change = change_y_opt(new_order, dist_matrix, num, i, j)
                if change:
                    new_order[i:j] = new_order[j - 1:i - 1:-1]
                    improved = True
                    replace += 1
    tour = np.array([points[new_order[i]] for i in range(num)])
    return new_order, tour_init, tour, replace


if __name__ == '__main__':
    number_points = 30
    rng = np.random.default_rng(4)
    data = rng.random((number_points, 2))

    order, matrix = utils.initial_tour(number_points, data, False, 0)
    _, init_tour, y_opt_tour, _ = y_opt_func(number_points, data, order, matrix)

    print(f'Construction tour length: {utils.tour_length(init_tour)}'
          f'\nY-opt tour length: {utils.tour_length(y_opt_tour)}')
    utils.show_tour(init_tour, y_opt_tour)
