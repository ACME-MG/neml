import sys; sys.path += ["../.."]
from moga_neml.api import API

api = API("plot", output_here=True, input_path="../data", output_path="../results")
api.define_model("evpcd")

api.read_data("creep/inl_1/AirBase_900_36_G22.csv")
api.add_error("dummy")
api.read_data("creep/inl_1/AirBase_900_31_G50.csv")
api.add_error("dummy")
api.read_data("creep/inl_1/AirBase_900_28_G45.csv")
api.add_error("dummy")
api.read_data("creep/inl_1/AirBase_900_26_G59.csv")
api.remove_oxidation()
api.add_error("dummy")
api.read_data("tensile/inl/AirBase_900_D10.csv")
api.add_error("dummy")

params_str = """
7.1037	48.235	4.2972	3.4084	1829.9	1433	4.6206	4.3208
3.0461	19.608	32.421	3.2736	2022.3	2114.8	4.479	13.783
4.634	18.607	24.896	3.3436	1999.7	2639.7	4.377	21.834

"""
params_list = [list(map(float, line.split())) for line in params_str.strip().split("\n")]

api.plot_predictions(
    params_list = params_list,
    limits_dict = {"creep": ((0, 7000), (0, 0.35)), "tensile": ((0, 1.0), (0, 250))},
)

# api.plot_distribution(
#     params_list = params_list,
#     limits_dict = {"evp_s0": (0, 40), "evp_R": (0, 500), "evp_d": (0, 50), "evp_n": (0, 10), "evp_eta": (0, 4000)},
#     # log=True,
# )
