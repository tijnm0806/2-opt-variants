import utils
import numpy as np
import time


def three_opt_func(num, points, init_order, dist_matrix):
    tour_init = points[init_order]
    new_order = init_order.copy()
    improved = True
    replace = 0
    while improved:
        improved = False
        for i in range(1, num - 3):
            for j in range(i + 2, num - 1):
                for k in range(j + 2, num + 1):
                    if i == 1 and k == num:
                        continue
                    t1, h1 = new_order[i - 1], new_order[i]
                    t2, h2 = new_order[j - 1], new_order[j]
                    t3, h3 = new_order[k - 1], new_order[k % num]
                    move = which_move(dist_matrix, t1, h1, t2, h2, t3, h3)
                    if move != 0:
                        improved = True
                        new_order = swap_order(new_order, move, i, j, k)
                        replace += 1
    tour = np.array([points[new_order[i]] for i in range(num)])
    return new_order, tour_init, tour, replace


def which_move(distances, t1, h1, t2, h2, t3, h3):
    ell_t1_h1, ell_t2_h2, ell_t3_h3 = distances[t1, h1], distances[t2, h2], distances[t3, h3]
    ell_t1_t2, ell_t2_t3, ell_t1_t3 = distances[t1, t2], distances[t2, t3], distances[t1, t3]
    ell_h1_h2, ell_h2_h3, ell_h1_h3 = distances[h1, h2], distances[h2, h3], distances[h1, h3]
    ell_t2_h3, ell_h1_t3, ell_t1_h2 = distances[t2, h3], distances[h1, t3], distances[t1, h2]

    change = np.array([0.0] * 8)

    change[0] = ell_t1_h1 + ell_t2_h2 + ell_t3_h3
    change[1] = ell_t1_h1 + ell_t2_t3 + ell_h2_h3
    change[2] = ell_t2_h2 + ell_t1_t3 + ell_h1_h3
    change[3] = ell_t3_h3 + ell_t1_t2 + ell_h1_h2
    change[4] = ell_h1_h2 + ell_t1_t3 + ell_t2_h3
    change[5] = ell_h2_h3 + ell_t1_t2 + ell_h1_t3
    change[6] = ell_h1_h3 + ell_t2_t3 + ell_t1_h2
    change[7] = ell_t2_h3 + ell_h1_t3 + ell_t1_h2

    return np.argmin(change)


def swap_order(old_order, case, p1, p2, p3):
    A = old_order[:p1]
    B = old_order[p1:p2]
    C = old_order[p2:p3]
    D = old_order[p3:]

    if case == 1:
        return np.concatenate((A, B, C[::-1], D))
    elif case == 2:
        return np.concatenate((A, C[::-1], B[::-1], D))
    elif case == 3:
        return np.concatenate((A, B[::-1], C, D))
    elif case == 4:
        return np.concatenate((A, C[::-1], B, D))
    elif case == 5:
        return np.concatenate((A, B[::-1], C[::-1], D))
    elif case == 6:
        return np.concatenate((A, C, B[::-1], D))
    else:
        return np.concatenate((A, C, B, D))


if __name__ == '__main__':
    number_points = 50
    rng = np.random.default_rng(3)
    data = rng.random((number_points, 2))

    start1 = time.time()
    order, matrix = utils.initial_tour(number_points, data, False, 0)
    _, init_tour, three_opt_tour, _ = three_opt_func(number_points, data, order, matrix)
    end1 = time.time()
    print(f'Running time: {end1 - start1}')

    print(f'Construction tour length: {utils.tour_length(init_tour)}'
          f'\n3-opt tour length: {utils.tour_length(three_opt_tour)}')
    utils.show_tour(init_tour, three_opt_tour)
