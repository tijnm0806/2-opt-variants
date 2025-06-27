# 2-opt variants python code
This repository contains the Python code developed and used for my bachelor thesis on the approximation ratios of local search variants for the Traveling Salesperson Problem (TSP). The focus lies on analyzing and comparing different heuristics based on 2-opt. The code is intended to provide the numerical results presented in the thesis and to generate visualizations used for the poster.

## main.py
This is the main script that runs the TSP solver using various 2-opt variants. The user can specify parameters such as the number of points in the TSP instance, a random seed for reproducibility, whether to use a randomly generated Euclidean instance or a predefined instance from a .tsp file, the desired local search algorithm (2-opt, x-opt, y-opt, z-opt, or 3-opt), and the number of samples to average results over.

The script returns the optimized tour length(s) and the number of edge replacements performed. If only one sample is used, a visualization of the initial and final tours is shown. Note that this code is designed specifically for two-dimensional Euclidean TSP instances.
