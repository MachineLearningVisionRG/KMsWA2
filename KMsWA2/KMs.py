import math
import numpy as np
from scipy.special import poch
from PIL import Image


def KMrec(N, M, p1, p2, Q, order):
    Wx = Weight_Function(p1, N - 1)
    Wy = Weight_Function(p2, M - 1)

    Kn = Krawtchouk_bar_poly(p1, order, N - 1, Wx)
    Km = Krawtchouk_bar_poly(p2, order, M - 1, Wy)
    Rec_F = np.zeros(shape=(N, M))
    for x in range(N):
        for y in range(M):
            Rec_F[x, y] = np.sum((Kn[:, x] * Km[:, y].reshape(-1, 1)) * Q)

    return Rec_F




def KMs(img, p, q, p1, p2, mthd):
    if mthd == 'Direct':
        Moms, Pols = Direct_mthd(img, p, q, p1, p2)
    else:
        print('This method is not supported')
    return Moms, Pols



def Direct_mthd(img, order, rep, p1, p2):
    Pols = []
    N, M = img.shape
    Moms = np.zeros(shape=(order + 1, rep + 1))
    Wx = Weight_Function(p1, N - 1)
    Wy = Weight_Function(p2, M - 1)

    Kp = Krawtchouk_bar_poly(p1, order, N - 1, Wx)
    Kq = Krawtchouk_bar_poly(p2, rep, M - 1, Wy)
    for p in range(order + 1):
        for q in range(rep + 1):
            Moms[p, q] = np.sum(((Kp[p,:].reshape(-1,1)) * Kq[q,:]) * img)
    # print(Moms.shape)
    Pols1 = Kp
    Pols2 = Kq
    Pols.append(Pols1)
    Pols.append(Pols2)
    return Moms, Pols


def Weight_Function(p, N):
    w = np.zeros(shape=(N+1), dtype=np.float64)
    w[0] = (1 - p) ** N
    for x in range(N):
        w[x + 1] = ((N-x)/(x+1))*(p/(1-p)) * w[x]
    return w


def p_norm(n, p, N):
    pnorm = ((-1)**n) * (((1-p)/p)**n) * (math.factorial(n)/poch(-N,n))
    return pnorm


def Krawtchouk_bar_poly(p, nmax, N, w):
    x = np.arange(N + 1)
    K = np.zeros(shape=(nmax + 1, N + 1), dtype=np.float64)
    if nmax == 0:
        K[0, :] = np.sqrt(w / p_norm(0, p, N))
    elif nmax == 1:
        x1 = (1-(x/(p*N)))
        y = p_norm(1, p, N)
        x2 = np.sqrt(w / y)
        K[1, :] = x1 * x2
    else:
        K[0, :] = np.sqrt(w / p_norm(0, p, N))
        x1 = (1 - (x / (p * N)))
        x2 = np.sqrt(w / p_norm(1, p, N))
        K[1, :] = (x1 * x2)
        for n in range(1, nmax):
            A = np.sqrt(p * (N - n) / ((1 - p) * (n + 1)))
            B = np.sqrt((p ** 2) * (N - n) * (N - n + 1) / (((1 - p) ** 2) * (n + 1) * n))
            x3 = A * (N * p - 2 * n * p + n - x)
            x4 = (K[n, :] - B * n * (1 - p) * K[n-1, :]) / (p * (N - n))
            K[n + 1, :] = (A * (N * p - 2 * n * p + n - x) * K[n, :] - B * n * (1 - p) * K[n-1, :]) / (p * (N - n))

    return K
# img = np.array(Image.open('les.jpg'))
# M, P = KMs(img, 32, 5, 0.5, 0.5, 'Direct')
K = KMrec(255, 255, 0.5, 0.5, 20, 30)
print(K[99,50])










