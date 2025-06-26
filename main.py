import utils
from tqdm import tqdm
import numpy as np
import two_opt
import x_opt
import y_opt
import z_opt
import three_opt


def main_function(n, seed, typ, file, alg, samples):
    seeds = [seed + j for j in range(samples)]
    opt_length = []
    if typ == 'Euclidean':
        for i in tqdm(range(samples)):
            rng = np.random.default_rng(seeds[i])
            points = rng.random((n, 2))
            order, matrix = utils.initial_tour(n, points, False, 0)
            _, init_tour, tour, rep = which_algorithm(n, points, order, matrix, alg)
            opt_length.append(utils.tour_length(tour))
    elif typ == 'file':
        graph, dist_matrix, n = utils.tsp_library_loader(file, seed)
        order, matrix = utils.initial_tour(n, graph, True, dist_matrix)
        opt_order, init_tour, tour, rep = which_algorithm(n, graph, order, matrix, alg)
        opt_length.append(utils.tsplib_length(n, opt_order, dist_matrix))
    else:
        raise Exception('Invalid graph type')
    if samples == 1 or typ == 'file':
        utils.show_tour(init_tour, tour)

    return opt_length, rep, tour


def which_algorithm(num, points, order, matrix, alg):
    if alg == '2-opt':
        opt_order, init_tour, tour, rep = two_opt.two_opt_func(num, points, order, matrix)
    elif alg == 'x-opt':
        opt_order, init_tour, tour, rep = x_opt.x_opt_func(num, points, order, matrix)
    elif alg == 'y-opt':
        opt_order, init_tour, tour, rep = y_opt.y_opt_func(num, points, order, matrix)
    elif alg == 'z-opt':
        opt_order, init_tour, tour, rep = z_opt.z_opt_func(num, points, order, matrix)
    elif alg == '3-opt':
        opt_order, init_tour, tour, rep = three_opt.three_opt_func(num, points, order, matrix)
    else:
        raise Exception('Invalid algorithm')
    return opt_order, init_tour, tour, rep


if __name__ == '__main__':
    num_vertices = 30
    set_seed = 4
    type_graph = 'file'                 # Euclidean, file
    file_path = 'tsplibrary/eil51.tsp'  # Only used when type_graph='file', only symmetric TSP works
    algorithm = 'z-opt'                     # 2-opt, x-opt, y-opt, z-opt, 3-opt
    num_samples = 1                        # Must equal 1 for a plot

    result, replacements, _ = main_function(num_vertices, set_seed, type_graph, file_path, algorithm, num_samples)
    print(f'The average tour length is: {np.average(result)}.')
    print(f'The average number of edge replacements is: {np.average(replacements)}.')

    # Poster
    # result1, _, t2 = main_function(num_vertices, set_seed, type_graph, file_path, '2-opt', num_samples)
    # result2, _, tx = main_function(num_vertices, set_seed, type_graph, file_path, 'x-opt', num_samples)
    # result3, _, ty = main_function(num_vertices, set_seed, type_graph, file_path, 'y-opt', num_samples)
    # result4, _, tz = main_function(num_vertices, set_seed, type_graph, file_path, 'z-opt', num_samples)
    # utils.poster_visual(t2, tx, ty, tz)
