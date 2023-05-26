# Libraries
import matplotlib.pyplot as plt
import numpy as np, math
from copy import deepcopy
from scipy.interpolate import splev, splrep, splder

# The Interpolator Class
class Interpolator:

    # Constructor
    def __init__(self, x_list, y_list, resolution=50, smooth=False):
        thin_indexes = get_thin_indexes(len(x_list), resolution)
        thin_x_list = [x_list[i] for i in thin_indexes]
        thin_y_list = [y_list[i] for i in thin_indexes]
        smooth_amount = resolution if smooth else 0
        self.spl = splrep(thin_x_list, thin_y_list, s=smooth_amount)
    
    # Convert to derivative
    def differentiate(self):
        self.spl = splder(self.spl)

    # Evaluate
    def evaluate(self, x_list):
        return list(splev(x_list, self.spl))

# Returns a list of indexes corresponding to thinned data
def get_thin_indexes(src_data_size, dst_data_size):
    step_size = src_data_size/dst_data_size
    thin_indexes = [math.floor(step_size*i) for i in range(1,dst_data_size-1)]
    thin_indexes = [0] + thin_indexes + [src_data_size-1]
    return thin_indexes

# For differentiating a curve
def differentiate_curve(curve):
    curve= deepcopy(curve)
    interpolator = Interpolator(curve["x"], curve["y"])
    interpolator.differentiate()
    curve["y"] = interpolator.evaluate(curve["x"])
    return curve

# Converts a CSV filename into a dictionary
def get_curve(file_name):

    # Read data
    file = open(file_name, "r")
    headers = file.readline().replace("\n","").split(",")
    data = [line.replace("\n","").split(",") for line in file.readlines()]
    file.close()
    
    # Get x and y data
    x_index = headers.index("x")
    y_index = headers.index("y")
    x_list = [float(d[x_index]) for d in data]
    y_list = [float(d[y_index]) for d in data]

    # Get auxiliary information
    curve_dict = {"x": x_list, "y": y_list}
    for i in range(len(headers)):
        if not headers[i] in ["x", "y"]:
            try:
                value = float(data[0][i])
            except:
                value = data[0][i]
            curve_dict[headers[i]] = value
    return curve_dict

# File names
file_list = [
    {"file_name": "AirBase_800_60_G32.csv"},
    {"file_name": "AirBase_800_65_G33.csv"},
    {"file_name": "AirBase_800_70_G44.csv"},
    {"file_name": "AirBase_800_80_G25.csv"},
]

# Initialise
curve_list = [get_curve(file["file_name"]) for file in file_list]
work_failure_list = []
avg_work_rate_list = []

# Iterate through curves
for curve in curve_list:

    # work to failure
    work_failure = curve["y"][-1] * curve["stress"]
    work_failure_list.append(work_failure)

    # Get average work rate
    d_curve = differentiate_curve(curve)
    work_rate_list = [curve["stress"] * dy for dy in d_curve["y"]]
    avg_work_rate = math.log10(np.average(work_rate_list))
    avg_work_rate_list.append(avg_work_rate)
    
    # Plot the results
    plt.scatter([avg_work_rate], [work_failure])

# Gets the gradient and intercept
polynomial = np.polyfit(avg_work_rate_list, work_failure_list, 1)
print(f"M = {polynomial[1]}") # 61.96
print(f"B = {polynomial[0]}") # 19.62

# Save the plot
plt.legend([curve["stress"] for curve in curve_list] + ["LOBF"])
plt.savefig("plot")