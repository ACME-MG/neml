import sys; sys.path += ["../.."]
from moga_neml.api import API

api = API("plot", output_here=True, input_path="../data", output_path="../results")
api.define_model("evpcd")

api.read_data("creep/inl_1/AirBase_800_80_G25.csv")
api.add_error("dummy")
api.read_data("creep/inl_1/AirBase_800_70_G44.csv")
api.add_error("dummy")
api.read_data("creep/inl_1/AirBase_800_65_G33.csv")
api.add_error("dummy")
api.read_data("creep/inl_1/AirBase_800_60_G32.csv")
api.add_error("dummy")
api.read_data("tensile/inl/AirBase_800_D7.csv")
api.add_error("dummy")

params_str = """
37.742	49.123	2.4996	3.4102	3172	2704.5	5.1187	9.9024
"""
params_list = [list(map(float, line.split())) for line in params_str.strip().split("\n")]

api.plot_predictions(
    params_list = params_list,
    limits_dict = {"creep": ((0, 8000), (0, 0.7)), "tensile": ((0, 1.0), (0, 500))},
)

api.plot_distribution(
    params_list = params_list,
    limits_dict = {"evp_s0": (0, 40), "evp_R": (0, 500), "evp_d": (0, 50), "evp_n": (0, 10), "evp_eta": (0, 4000),
                   "cd_A": (0, 5000), "cd_xi": (0, 10), "cd_phi": (0, 30)},
)
