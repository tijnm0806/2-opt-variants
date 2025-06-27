# 2-opt variants python code
This repository contains the Python code developed and used for my bachelor thesis on the approximation ratios of local search variants for the Traveling Salesperson Problem (TSP). The focus lies on analyzing and comparing different heuristics based on 2-opt. The code is intended to provide the numerical results presented in the thesis and to generate visualizations used for the poster. Below is a short description of the main files included in this repository.

## main.py
This is the main script that runs the TSP solver using various 2-opt variants. The user can specify parameters such as the number of points in the TSP instance, a random seed for reproducibility, whether to use a randomly generated Euclidean instance or a predefined instance from a .tsp file, the desired local search algorithm (2-opt, x-opt, y-opt, z-opt, or 3-opt), and the number of samples to average results over.

The script returns the optimized tour length(s) and the number of edge replacements performed. If only one sample is used, a visualization of the initial and final tours is shown. Note that this code is designed specifically for two-dimensional Euclidean TSP instances.

## two_opt.py
This file implements the 2-opt local search heuristic for the TSP. Starting from an initial tour, it iteratively checks all pairs of non-adjacent edges and applies the 2-opt swap if it results in a shorter tour. The function returns the improved tour, the original tour, and the number of edge replacements made. While the file is primarily intended to be called from main.py, it can also be run on its own to apply 2-opt to a random TSP instance and visualize the result.

## x_opt.py
This file implements the X-opt heuristic, a geometric variant of 2-opt that focuses on removing crossings in the tour. Instead of comparing edge lengths, it checks for intersecting edges using orientation tests and performs a x-opt swap when a crossing is detected. While designed to be used via main.py, the file can also be run independently to apply X-opt to a random TSP instance and visualize the result.

## y_opt.py
This file implements the Y-opt heuristic, a restricted 2-opt variant that only accepts edge swaps if both new edges are strictly better than the ones they replace. The decision is based on comparing the maximum and minimum lengths of the old and new edge pairs. While designed to be used via main.py, the file can also be run independently to apply Y-opt to a random TSP instance and visualize the result.

## z_opt.py
This file implements the Z-opt heuristic, a stricter variant of Y-opt that only accepts a 2-opt move if both new edges are better than both old edges in all pairwise comparisons. This makes Z-opt more conservative, typically resulting in fewer replacements but potentially higher-quality improvements. Like the other heuristics, it is meant to be used through main.py but can also be executed on its own for testing and visualization.

## three_opt.py
This file implements the 3-opt local search heuristic for the TSP. The function returns the improved tour, the original tour, and the number of edge replacements made. While the file is primarily intended to be called from main.py, it can also be run on its own to apply 3-opt to a random TSP instance and visualize the result.

## utils.py
This utility file provides essential helper functions used throughout the repository, including distance matrix computation, tour initialization, heuristic construction methods, and tour visualization. It also contains routines for working with TSPLIB instances and generating comparative plots. While not intended to be executed on its own, it supports all algorithm files and is vital for both performance evaluation and graphical presentation.

## plot_data.py
This script is only used to visualize numerical results for different 2-opt variants. It plots average tour lengths and average numbers of edge replacements agains the instance size (number of points), both in raw and normalized forms.


**Note:** Some parts of the code descriptions were generated with the assistance of ChatGPT (GPT-4o-mini), an AI language model developed by OpenAI.
