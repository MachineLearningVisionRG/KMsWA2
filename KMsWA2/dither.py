import math
import numpy as np


def dither(z_pq_v_c, b_seq, delta, d_0):
    z_pq_mod_v = np.zeros(1)
    z_pq_magn_v_c = abs(z_pq_v_c)

    for i in range(2):
        d_1 = delta/2 + d_0
        if b_seq == 1:
            z_pq_magn_mod_v = np.round(((z_pq_magn_v_c - d_1) / delta)) * delta + d_1
            z_pq_mod_v = (z_pq_magn_mod_v / z_pq_magn_v_c) * z_pq_v_c
        else:
            z_pq_magn_mod_v = np.round(((z_pq_magn_v_c - d_0) / delta)) * delta + d_0
            z_pq_mod_v = (z_pq_magn_mod_v / z_pq_magn_v_c) * z_pq_v_c

        min_dist = (z_pq_magn_mod_v - z_pq_magn_v_c) ** 2
    return z_pq_mod_v, min_dist


# print(dither(17.25, 0, 5, 2.5))