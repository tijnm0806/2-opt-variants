import numpy as np
import matplotlib.pyplot as plt
# plt.rcParams.update({'font.size': 15, 'axes.titlesize': 20, 'axes.labelsize': 20, 'xtick.labelsize': 16,
#                      'ytick.labelsize': 12, 'legend.fontsize': 13})


def plot_average(two, x, y, z, steps):
    n = np.array([200 * i for i in range(1, 11)])
    if steps:
        normalization = n
    else:
        normalization = n ** 0.5
    n_two = two / normalization
    n_x = x / normalization
    n_y = y / normalization
    n_z = z / normalization

    plt.figure(figsize=(8, 3.5))
    plt.subplot(1, 2, 1)
    plt.plot(n, two, label='2-opt', marker='o', linestyle='-', markersize=5, linewidth=2)
    plt.plot(n, x, label='X-opt', marker='o', linestyle='-', markersize=5, linewidth=2)
    plt.plot(n, y, label='Y-opt', marker='o', linestyle='-', markersize=5, linewidth=2)
    plt.plot(n, z, label='Z-opt', marker='o', linestyle='-', markersize=5, linewidth=2)
    plt.xlabel("n")
    if steps:
        plt.ylabel("Avg. edge replacements")
    else:
        plt.ylabel("Average tour length")
    plt.grid(True)
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(n, n_two, label='2-opt', marker='o', linestyle='-', markersize=5, linewidth=2)
    plt.plot(n, n_x, label='X-opt', marker='o', linestyle='-', markersize=5, linewidth=2)
    plt.plot(n, n_y, label='Y-opt', marker='o', linestyle='-', markersize=5, linewidth=2)
    plt.plot(n, n_z, label='Z-opt', marker='o', linestyle='-', markersize=5, linewidth=2)
    plt.xlabel("n")
    if steps:
        plt.ylabel("Avg. edge replacements / n")
    else:
        plt.ylabel("Average tour length / √n")
    plt.grid(True)

    plt.tight_layout()
    plt.show()


def plot_steps(size, step_2, step_x, step_y, step_z, step_3):

    plt.figure(figsize=(8, 3.5))
    plt.subplot(1, 2, 1)
    plt.scatter(size, step_2, s=10, label='2-opt', marker='o')
    plt.scatter(size, step_x, s=10, label='X-opt', marker='o')
    plt.scatter(size, step_y, s=10, label='Y-opt', marker='o')
    plt.scatter(size, step_z, s=10, label='Z-opt', marker='o')
    plt.scatter(size, step_3, s=10, label='3-opt', marker='o')
    plt.xlabel("n")
    plt.ylabel("Number of edge replacements")
    plt.grid(True)
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.scatter(size, step_2 / size, s=10, label='2-opt', marker='o')
    plt.scatter(size, step_x / size, s=10, label='X-opt', marker='o')
    plt.scatter(size, step_y / size, s=10, label='Y-opt', marker='o')
    plt.scatter(size, step_z / size, s=10, label='Z-opt', marker='o')
    plt.scatter(size, step_3 / size, s=10, label='3-opt', marker='o')
    plt.xlabel("n")
    plt.ylabel("Number of edge replacements / n")
    plt.grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # Plot the average tour length as n grows for different 2-opt variants
    av_2_opt = np.array([11.88886881, 16.65401232, 20.32368067, 23.39599824, 26.1128789,
                         28.56344067, 30.82753092, 32.92765206, 34.89401298, 36.76557068])
    av_y_opt = np.array([12.72039423, 17.79736179, 21.69012605, 24.98501615, 27.86125441,
                         30.48330593, 32.87963935, 35.11439862, 37.21778522, 39.19773561])
    av_z_opt = np.array([17.39794391, 24.46201105, 29.8165818, 34.40306404, 38.31247048,
                         41.93245319, 45.20888983, 48.27535213, 51.15535746, 53.87469906])
    av_x_opt = np.array([20.2548036, 29.07705851, 35.80828586, 41.53078056, 46.55820907,
                         51.07891143, 55.30547574, 59.131461, 62.786543, 66.2046426])
    plot_average(av_2_opt, av_x_opt, av_y_opt, av_z_opt, False)

    # Plot the average number of edge replacements as n grows for different 2-opt variants
    av_x_opt_steps = np.array([464.374, 1126.4775, 1864.9865, 2655.5625, 3481.4475,
                               4344.626,  5221.628, 6133.6885, 7047.4185, 7993.475])
    av_2_opt_steps = np.array([712.2395, 1668.9415, 2719.677, 3831.708, 4988.6655,
                               6182.866, 7403.4505, 8653.2005, 9925.0415, 11210.1685])
    av_y_opt_steps = np.array([456.396, 1071.7205, 1744.278, 2455.975, 3192.31,
                               3953.4375, 4734.365, 5527.805, 6336.7845, 7156.171])
    av_z_opt_steps = np.array([263.496, 630.561, 1037.228, 1469.0545, 1921.472,
                               2387.829, 2866.0955, 3356.8425, 3855.115, 4361.4705])
    plot_average(av_2_opt_steps, av_x_opt_steps, av_y_opt_steps, av_z_opt_steps, True)
