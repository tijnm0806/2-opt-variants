import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt
from scipy.spatial import distance
import tsplib95
plt.rcParams.update({'font.size': 10, 'axes.titlesize': 10, 'axes.labelsize': 10, 'xtick.labelsize': 10,
                     'ytick.labelsize': 10, 'legend.fontsize': 10})


def distance_matrix(points):
    return distance.cdist(points, points, 'euclidean')


def initial_tour(num, points, has_matrix, distance_mat):
    if not has_matrix:
        distance_mat = distance_matrix(points)
    tour_order = np.arange(num)
    # tour_order = nearest_neighbour(num, distance_mat)
    # tour_order = double_nearest_neighbour(num, distance_mat)
    return tour_order, distance_mat


def nearest_neighbour(num, distances):
    unvisited = set(range(1, num))
    near_tour = [0]
    current = 0
    while unvisited:
        current = min(unvisited, key=lambda point: distances[current, point])
        near_tour.append(current)
        unvisited.remove(current)
    return near_tour


def double_nearest_neighbour(num, distances):
    unvisited = set(range(1, num))
    near_tour = [0]
    right = 0
    left = 0
    while unvisited:
        right = min(unvisited, key=lambda point: distances[right, point])
        unvisited.remove(right)
        near_tour.append(right)
        if unvisited:
            left = min(unvisited, key=lambda point: distances[left, point])
            unvisited.remove(left)
            near_tour.insert(0, left)
    return near_tour


def tour_length(points):
    return np.sum([norm(points[i] - points[i - 1]) for i in range(len(points))])


def tsplib_length(num, points, distances):
    total_length = 0
    for v in range(num):
        total_length += distances[points[v-1]][points[v]]
    return total_length


def show_tour(init_tour, new_tour):
    x, y = np.append(init_tour[:, 0], init_tour[0, 0]), np.append(init_tour[:, 1], init_tour[0, 1])
    u, v = np.append(new_tour[:, 0], new_tour[0, 0]), np.append(new_tour[:, 1], new_tour[0, 1])

    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.plot(x, y, marker='o', linestyle='-', color='black', markersize=7, markerfacecolor='red')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Initial Tour")
    # plt.axis('off')
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(u, v, marker='o', linestyle='-', color='black', markersize=7, markerfacecolor='red')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("2-opt (variant) Optimal Tour")
    plt.grid(True)
    # plt.axis('off')
    plt.tight_layout()
    plt.show()


def tsp_library_loader(file_name, seed):
    problem = tsplib95.load(file_name)
    if problem.type != 'TSP' or problem.edge_weight_type != 'EUC_2D':
        raise Exception(f'Invalid graph type. Only symmetric TSP with euclidean distances allowed')

    vertices = np.array(list(problem.node_coords.values()), dtype=np.float64)
    rng = np.random.default_rng(seed)
    vertices = np.unique(vertices, axis=0)
    vertices = vertices[rng.permutation(len(vertices))]
    num = len(vertices)
    # print(f'Number of unique points: {num}.')

    dist_matrix = distance.cdist(vertices, vertices, lambda u, v: round(np.sqrt(((u-v)**2).sum())))
    return vertices, dist_matrix, num


def poster_visual(tour_2, tour_x, tour_y, tour_z):
    a, b = np.append(tour_2[:, 0], tour_2[0, 0]), np.append(tour_2[:, 1], tour_2[0, 1])
    u, v = np.append(tour_x[:, 0], tour_x[0, 0]), np.append(tour_x[:, 1], tour_x[0, 1])
    x, y = np.append(tour_y[:, 0], tour_y[0, 0]), np.append(tour_y[:, 1], tour_y[0, 1])
    p, q = np.append(tour_z[:, 0], tour_z[0, 0]), np.append(tour_z[:, 1], tour_z[0, 1])

    plt.figure(figsize=(10, 3))
    plt.subplot(1, 4, 1)
    plt.plot(a, b, marker='o', linestyle='-', color='black', markersize=8, markerfacecolor='red', linewidth=1.7)
    plt.title("2-optimal")
    plt.axis('off')

    plt.subplot(1, 4, 2)
    plt.plot(u, v, marker='o', linestyle='-', color='black', markersize=8, markerfacecolor='red', linewidth=1.7)
    plt.title("X-optimal")
    plt.axis('off')

    plt.subplot(1, 4, 3)
    plt.plot(x, y, marker='o', linestyle='-', color='black', markersize=8, markerfacecolor='red', linewidth=1.7)
    plt.title("Y-optimal")
    plt.axis('off')

    plt.subplot(1, 4, 4)
    plt.plot(p, q, marker='o', linestyle='-', color='black', markersize=8, markerfacecolor='red', linewidth=1.7)
    plt.title("Z-optimal")
    plt.axis('off')

    plt.tight_layout(w_pad=4.0)
    plt.show()
