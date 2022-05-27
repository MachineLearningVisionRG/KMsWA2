import numpy as np

def zigzag(in_):
    h = 0
    v = 0
    vmin = 0
    hmin = 0
    vmax = in_.shape[0]
    hmax = in_.shape[1]
    i = 0
    output = np.zeros((vmax * hmax))

    while ((v <= vmax) and (h <= hmax) ):
        if ((h + v) % 2) == 0:  # going up
            if (v == vmin):
                output[i] = in_[v, h]  # if we got to the first line
                if (h == hmax - 1):
                    v = v + 1
                else:
                    h = h + 1

                i = i + 1

            elif ((h == hmax - 1) and (v < vmax)):  # if we got to the last column
                output[i] = in_[v, h]
                v = v + 1
                i = i + 1

            elif ((v > vmin) and (h < hmax - 1)):  # all other cases
                output[i] = in_[v, h]
                v = v - 1
                h = h + 1
                i = i + 1


        else:  # going down

            if ((v == vmax - 1) and (h <= hmax - 1)):  # if we got to the last line
                output[i] = in_[v, h]
                h = h + 1
                i = i + 1

            elif (h == hmin):  # if we got to the first column
                output[i] = in_[v, h]
                if (v == vmax - 1):
                    h = h + 1
                else:
                    v = v + 1

                i = i + 1

            elif ((v < vmax - 1) and (h > hmin)):  # all other cases
                output[i] = in_[v, h]
                v = v + 1
                h = h - 1
                i = i + 1

        if ((v == vmax - 1) and (h == hmax - 1)):  # bottom right element
            output[i] = in_[v, h]
            break

    return output


def inverse_zigzag(in_, vmax, hmax):
    h = 0
    v = 0
    vmin = 0
    hmin = 0
    output = np.zeros((vmax, hmax))
    i = 0
    while (v < vmax) and (h < hmax):
        if ((h + v) % 2) == 0:  # going up

            if v == vmin:
                output[v, h] = in_[i]  # if we got to the first line

                if h == hmax-1:
                    v = v + 1
                else:
                    h = h + 1

                i = i + 1

            elif (h == hmax - 1) and (v < vmax):  # if we got to the last column
                output[v, h] = in_[i]
                v = v + 1
                i = i + 1

            elif (v > vmin) and (h < hmax - 1):  # all other cases
                output[v, h] = in_[i]
                v = v - 1
                h = h + 1
                i = i + 1

        else:  # going down

            if (v == vmax - 1) and (h <= hmax - 1):  # if we got to the last line
                output[v, h] = in_[i]
                h = h + 1
                i = i + 1

            elif h == hmin:  # if we got to the first column
                output[v, h] = in_[i]
                if v == vmax - 1:
                    h = h + 1
                else:
                    v = v + 1
                i = i + 1

            elif (v < vmax - 1) and (h > hmin):  # all other cases
                output[v, h] = in_[i]
                v = v + 1
                h = h - 1
                i = i + 1

        if (v == vmax - 1) and (h == hmax - 1):  # bottom right element
            output[v, h] = in_[i]
            break

    return output


