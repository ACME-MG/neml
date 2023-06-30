"""
 Title:         Curve related Functions
 Description:   Contains functions to manipulate curves
 Author:        Janzen Choi

"""

# Libraries
import numpy as np
import math
from copy import deepcopy

# Returns the coordinates of non-outliers (good to use with derivatives)
def exclude_outliers(x_list, y_list):
    q_1 = np.percentile(y_list, 25)
    q_3 = np.percentile(y_list, 75)
    u_bound = q_3 + 1.5*(q_3-q_1)
    l_bound = q_1 - 1.5*(q_3-q_1)
    index_list = [i for i in range(len(y_list)) if y_list[i] >= l_bound and y_list[i] <= u_bound]
    x_list = [x_list[i] for i in index_list]
    y_list = [y_list[i] for i in index_list]
    return x_list, y_list

# Returns a sample creep curve
def get_sample_creep_curve():
    polynomial = [0.1, -0.6, 1.3, 0]
    x_list = [10*x for x in range(100)]
    scaled_x_list = [x/225 for x in x_list]
    y_list = list(np.polyval(polynomial, scaled_x_list))
    y_list = [y/8 for y in y_list]
    return {"x": x_list, "y": y_list}

# Returns a list of indexes corresponding to thinned data
def get_thin_indexes(src_data_size, dst_data_size):
    step_size = src_data_size/dst_data_size
    thin_indexes = [math.floor(step_size*i) for i in range(1,dst_data_size-1)]
    thin_indexes = [0] + thin_indexes + [src_data_size-1]
    return thin_indexes

# Returns a list of indexes corresponding to thinned data based on a defined cumulative distribution function
def get_custom_thin_indexes(src_data_size, dst_data_size, distribution):
    unmapped_indexes = [distribution(i/dst_data_size) for i in range(1,dst_data_size-1)]
    thin_indexes = [math.floor(i*src_data_size) for i in unmapped_indexes]
    thin_indexes = [0] + thin_indexes + [src_data_size-1]
    return thin_indexes

# Removes data after a specific x value of a curve
def remove_data_after(curve:dict, x_value:float) -> dict:
    new_curve = deepcopy(curve)
    new_curve["x"], new_curve["y"] = [], []
    for i in range(len(curve["x"])):
        if curve["x"][i] < x_value:
            new_curve["x"].append(curve["x"][i])
            new_curve["y"].append(curve["y"][i])
    return new_curve
