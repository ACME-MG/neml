import sys; sys.path += ["../.."]
from moga_neml.interface import Interface
from constants import PARAM_INDEX

itf = Interface("evpwdb f 900 st", input_path="../data", output_path="../results")

itf.define_model("evpwdb")

params_str = """
4.8238	378.86	0.1423	4.4021	1006.9
7.1037	48.235	4.2972	3.4084	1829.9
3.0461	19.608	32.421	3.2736	2022.3
4.634	18.607	24.896	3.3436	1999.7
16.287	181.45	0.52517	3.0161	2606.2
9.5313	148.61	0.37484	3.9621	1253.9
6.3647	149.54	0.43913	4.1839	1127.6
12.622	15.441	4.5386	3.7305	1371.6
12.256	273.68	0.20866	3.8422	1242.3
7.044	16.175	6.7949	4.1207	1090
"""
params_list = [list(map(float, line.split())) for line in params_str.strip().split("\n")]
itf.fix_params(params_list[PARAM_INDEX])

itf.read_data("creep/inl_1/AirBase_900_36_G22.csv")
itf.add_error("area", "time", "strain")
itf.add_error("end", "time")
itf.add_error("end", "strain")

itf.read_data("creep/inl_1/AirBase_900_31_G50.csv")
itf.add_error("area", "time", "strain")
itf.add_error("end", "time")
itf.add_error("end", "strain")

itf.read_data("creep/inl_1/AirBase_900_28_G45.csv")

itf.read_data("creep/inl_1/AirBase_900_26_G59.csv")
itf.remove_oxidation()

itf.read_data("tensile/inl/AirBase_900_D10.csv")
itf.add_error("area", "strain", "stress")
itf.add_error("end", "strain")
itf.add_error("arg_max", "strain", "stress")
itf.add_error("yield", yield_stress=164)

itf.reduce_errors("square_average")
itf.reduce_objectives("square_average")

itf.plot_experimental()
itf.set_recorder(10, plot_opt=True, plot_loss=True)
itf.optimise(10000, 100, 50, 0.8, 0.01)
