import utils
import numpy as np


def x_opt_func(num, points, init_order, dist_matrix):
    tour_init = points[init_order]
    new_order = init_order.copy()
    tour = tour_init.copy()
    improved = True
    replace = 0
    while improved:
        improved = False
        for i in range(1, num - 1):
            for j in range(i + 2, num + 1):
                if i == 1 and j == num:
                    continue
                cross = crossing_new(tour, num, i, j)
                if cross:
                    tour[i:j] = tour[j - 1:i - 1:-1]
                    new_order[i:j] = new_order[j - 1:i - 1:-1]
                    improved = True
                    replace += 1
    return new_order, tour_init, tour, replace


def crossing_new(points, num, p, q):
    t1, h1 = points[p - 1], points[p]
    t2, h2 = points[q - 1], points[q % num]

    e = h1 - t1
    f = h2 - t2

    cross1 = cross_product(e, t2 - t1)
    cross2 = cross_product(e, h2 - t1)
    cross3 = cross_product(f, t1 - t2)
    cross4 = cross_product(f, h1 - t2)

    if (cross1 * cross2 < 0) and (cross3 * cross4 < 0):
        return True
    if cross1 == 0 and on_segment(t1, t2, h1):
        return True
    if cross2 == 0 and on_segment(t1, h2, h1):
        return True
    if cross3 == 0 and on_segment(t2, t1, h2):
        return True
    if cross4 == 0 and on_segment(t2, h1, h2):
        return True
    else:
        return False


def cross_product(a, b):
    return a[0] * b[1] - a[1] * b[0]


def on_segment(a, b, c):
    return min(a[0], c[0]) <= b[0] <= max(a[0], c[0]) and min(a[1], c[1]) <= b[1] <= max(a[1], c[1])


if __name__ == '__main__':
    number_points = 30
    rng = np.random.default_rng(4)
    data = rng.random((number_points, 2))

    order, matrix = utils.initial_tour(number_points, data, False, 0)
    _, init_tour, x_opt_tour, _ = x_opt_func(number_points, data, order, matrix)

    print(f'Construction tour length: {utils.tour_length(init_tour)},'
          f'\nX-opt tour length: {utils.tour_length(x_opt_tour)}')
    utils.show_tour(init_tour, x_opt_tour)
