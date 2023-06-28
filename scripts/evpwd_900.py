import sys; sys.path += [".."]
from moga_neml.api import API

api = API("evpwd 900")
api.define_model("evpwd")

api.read_file("creep/inl_1/AirBase_900_36_G22.csv", True)
api.read_file("creep/inl_1/AirBase_900_31_G50.csv", True)
api.read_file("creep/inl_1/AirBase_900_28_G45.csv", False)
api.read_file("creep/inl_1/AirBase_900_26_G59.csv", False)
api.remove_oxidised_creep(100, 0.7)
api.read_file("tensile/AirBase_900_D10.csv", True)

api.visualise(type="creep")
api.visualise(type="tensile")
api.add_error("y_area", "creep")
api.add_error("x_end", "creep")
api.add_error("y_end", "creep")
api.add_error("y_area", "tensile")
api.record(10, 10)
api.optimise(10000, 200, 100, 0.65, 0.35)