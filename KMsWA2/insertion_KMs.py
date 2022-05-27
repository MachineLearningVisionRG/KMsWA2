import numpy as np
from matplotlib import pyplot as plt
from KMs import KMs, KMrec
from zigzag import zigzag, inverse_zigzag
from dither import dither
from PIL import Image


def insertion_KMs(img, b_seq, order, delta, p1, p2, numbits):
    # Moments Calculation
    moments, KPols = KMs(img, order, order, p1, p2, 'Direct')

    # Moments choice
    mom_all_orig_v = zigzag(moments)
    water_info = np.zeros(shape=(mom_all_orig_v.shape[0]))
    mom_all_mod = [0]
    for i in range(1, len(b_seq[:numbits]) + 1):
        mom_all_mod_list, min_dist = dither(mom_all_orig_v[i], b_seq[i-1], delta, delta/2)
        mom_all_mod.append(mom_all_mod_list)
        water_info[i] = mom_all_mod[i] - mom_all_orig_v[i]

    water_info = inverse_zigzag(water_info, moments.shape[0], moments.shape[1])
    Rec_F = KMrec(img.shape[0], img.shape[1], p1, p2, water_info, order)
    watermarked_img = img + Rec_F
    plt.imshow(watermarked_img, cmap='gray', vmin=0, vmax=255, interpolation='none')
    plt.show()
    plt.imsave('test.jpg', watermarked_img, cmap='gray', vmin=0, vmax=255)
    return watermarked_img





