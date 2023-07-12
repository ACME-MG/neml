import sys; sys.path += [".."]
from moga_neml.api import API

api = API("evpcd 900 init all")
api.define_model("evpcd")

api.init_param("evp_s0",  4.871e0)
api.init_param("evp_R",   1.152e1)
api.init_param("evp_d",   7.028e0)
api.init_param("evp_n",   4.242e0)
api.init_param("evp_eta", 1.138e3)

api.init_param("cd_A",    5.826e3)
api.init_param("cd_xi",   3.499e0)
api.init_param("cd_phi",  7.520e0)

api.read_data("tensile/AirBase_900_D10.csv")
api.add_error("y_area", "strain", "stress")
api.add_error("yield")

api.read_data("creep/inl_1/AirBase_900_36_G22.csv")
api.add_error("y_area", "time", "strain")
api.add_error("x_end", "time")
api.add_error("x_end", "strain")
api.add_error("damage")

api.read_data("creep/inl_1/AirBase_900_31_G50.csv")
api.add_error("y_area", "time", "strain")
api.add_error("x_end", "time")
api.add_error("x_end", "strain")
api.add_error("damage")

api.read_data("creep/inl_1/AirBase_900_28_G45.csv")
api.add_error("y_area", "time", "strain")
api.add_error("x_end", "time")
api.add_error("x_end", "strain")
api.add_error("damage")

api.read_data("creep/inl_1/AirBase_900_26_G59.csv")
api.remove_oxidation()
api.add_error("y_area", "time", "strain")
api.add_error("x_end", "time")
api.add_error("x_end", "strain")
api.add_error("damage")

api.reduce_errors("square_average")
api.reduce_objectives("square_average")

api.set_recorder(10, 10)
api.optimise(10000, 100, 50, 0.65, 0.35)
