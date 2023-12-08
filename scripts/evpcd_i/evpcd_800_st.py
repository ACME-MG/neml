import sys; sys.path += ["../.."]
from moga_neml.api import API

api = API("evpcd f 800 st", input_path="../data", output_path="../results")

api.define_model("evpcd")

params_str = """
31.327	104.92	0.8548	3.7508	2575.8	2126.4	5.3209	6.5504
22.393	462.57	0.13573	4.314	1828.1	1912.9	5.5169	6.9639
11.45	53.151	7.1666	3.9502	2221.6	4328.7	4.3679	5.3108
37.742	49.123	2.4996	3.4102	3172	2704.5	5.1187	9.9024
18.768	89.18	0.88069	4.5055	1677.4	2589.7	5.1066	8.5635
23.304	306.58	0.32123	4.2592	1822.6	2169.1	5.3202	6.8598
31.137	31.413	4.6003	3.6958	2583	2511.7	5.1559	8.7353
29.726	45.991	2.3174	3.9613	2101.3	2259.2	5.3187	8.5096
0.85682	42.524	9.6283	4.5033	1707	1896.9	5.547	6.8471
4.4611	35.628	31.021	3.6186	3016.2	3411.1	4.8323	12.863
"""
params_list = [list(map(float, line.split())) for line in params_str.strip().split("\n")]
api.init_params(params_list[1])

api.read_data("creep/inl_1/AirBase_800_80_G25.csv")
api.add_error("area", "time", "strain")
api.add_error("end", "time")
api.add_error("end", "strain")
api.add_constraint("inc_end", "strain")
api.add_constraint("dec_end", "time")

api.read_data("creep/inl_1/AirBase_800_70_G44.csv")
api.add_error("area", "time", "strain")
api.add_error("end", "time")
api.add_error("end", "strain")
api.add_constraint("inc_end", "strain")
api.add_constraint("dec_end", "time")

api.read_data("creep/inl_1/AirBase_800_65_G33.csv")

api.read_data("creep/inl_1/AirBase_800_60_G32.csv")

api.read_data("tensile/inl/AirBase_800_D7.csv")
api.add_error("area", "strain", "stress")
api.add_error("end", "strain")
api.add_error("arg_max", "strain", "stress", weight=0.5)
api.add_error("yield", yield_stress=291)
# api.add_error("end", "stress")

api.reduce_errors("square_average")
api.reduce_objectives("square_average")

api.plot_experimental()
api.set_recorder(10, True, True, True)
api.optimise(10000, 100, 50, 0.8, 0.01)