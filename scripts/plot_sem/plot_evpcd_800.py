import sys; sys.path += ["../.."]
from moga_neml.interface import Interface

itf = Interface("plot", output_here=True, input_path="../data", output_path="../results")
itf.define_model("evpcd")

itf.read_data("creep/inl_1/AirBase_800_80_G25.csv")
itf.add_error("dummy")
itf.read_data("creep/inl_1/AirBase_800_70_G44.csv")
itf.add_error("dummy")
itf.read_data("creep/inl_1/AirBase_800_65_G33.csv")
# itf.add_error("dummy")
itf.read_data("creep/inl_1/AirBase_800_60_G32.csv")
# itf.add_error("dummy")
itf.read_data("tensile/inl/AirBase_800_D7.csv")
itf.add_error("dummy")

params_str = """
16.994	187.83	0.26104	4.502	1784.8	3263.5	4.9231	13.172
22.454	66.77	0.92681	4.4191	1610.1	2142	5.4844	11.449
9.1648	36.326	12.337	4.2247	1776.1	2731	5.0411	8.3103
5.8951	36.907	5.3551	4.7311	1557.8	2224.1	5.2809	6.5113
4.1861	84.548	2.1125	4.767	1574.1	2883.2	4.8395	4.5431
27.868	89.339	0.59712	4.1982	1818	2645.2	5.1192	10.125
28.599	78.057	0.84292	3.8371	2441.5	2969.6	4.9976	10.642
29.979	119.58	0.552	3.8505	2314.4	2808.8	5.0354	9.5435
19.125	43.641	5.6148	4.1688	1616	1876.8	5.5594	6.8653
22.012	38.873	2.2033	4.245	1841.2	2377	5.2898	9.7712
31.647	120.62	0.85485	3.7266	2297.8	2165.7	5.3247	7.7724
33.297	522.85	0.11871	3.9767	1762.4	1913.8	5.6638	11.287
10.788	53.85	7.1746	3.8604	2196.3	3182.9	4.6458	3.7222
38.181	51.055	2.4819	3.2572	3154.4	2725.2	5.0167	8.33
24.889	44.932	1.2076	4.5055	1527.9	2589.7	5.1066	8.695
23.304	276.66	0.32123	4.2592	1767.2	2168.5	5.3181	6.7619
30.401	34.817	4.5983	3.5323	2583	2520.9	5.1559	8.5891
5.0569	40.476	10.017	4.1585	1730.1	1998.1	5.5564	10.337
31.809	43.194	2.2399	3.9613	1820.1	2245.4	5.3179	8.5096
0.36499	45.374	15.687	3.6105	2878.3	3325.8	4.847	12.328
"""
params_list = [list(map(float, line.split())) for line in params_str.strip().split("\n")]

itf.plot_simulations(
    params_list = params_list,
    limits_dict = {"creep": ((0, 8000), (0, 0.7)), "tensile": ((0, 1.0), (0, 500))},
)

itf.plot_distribution(
    params_list = params_list,
    limits_dict = {"evp_s0": (0, 40), "evp_R": (0, 500), "evp_d": (0, 50), "evp_n": (0, 10), "evp_eta": (0, 4000),
                   "cd_A": (0, 5000), "cd_xi": (0, 10), "cd_phi": (0, 30)},
)
