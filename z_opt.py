import utils
import numpy as np
import time


def change_z_opt(tour, distances, num, p, q):
    t1, h1 = tour[p - 1], tour[p]
    t2, h2 = tour[q - 1], tour[q % num]
    e1, e2 = distances[h1, t1], distances[h2, t2]
    e3, e4 = distances[t2, t1], distances[h2, h1]
    if e1 + e2 > e3 + e4:
        if e1 >= e3:
            if e1 >= e4:
                if e2 >= e3:
                    if e2 >= e4:
                        return True
    return False


def z_opt_func(num, points, init_order, dist_matrix):
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
                change = change_z_opt(new_order, dist_matrix, num, i, j)
                if change:
                    new_order[i:j] = new_order[j - 1:i - 1:-1]
                    improved = True
                    replace += 1
    tour = np.array([points[new_order[i]] for i in range(num)])
    return new_order, tour_init, tour, replace


if __name__ == '__main__':
    number_points = 50
    rng = np.random.default_rng(3)
    data = rng.random((number_points, 2))

    start1 = time.time()
    order, matrix = utils.initial_tour(number_points, data, False, 0)
    _, init_tour, z_opt_tour, _ = z_opt_func(number_points, data, order, matrix)
    end1 = time.time()
    print(end1 - start1)

    print(f'Construction tour length: {utils.tour_length(init_tour)}'
          f'\nZ-opt tour length: {utils.tour_length(z_opt_tour)}')
    utils.show_tour(init_tour, z_opt_tour)
