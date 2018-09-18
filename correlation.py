import math
import numpy as np


def corr(cov, xbar, ybar, mtx):

    stdx = 0
    stdy = 0

    def sq(num):
        return math.pow(num, 2)

    def st_dev(num):
        return math.sqrt(num/len(mtx))

    for i in range(len(mtx)):
        # stdX += math.pow(mtx[i][0]-xBar,2)
        # stdY += math.pow(mtx[i][1]-yBar,2)
        stdx += sq(mtx[i][0]-xbar)
        stdy += sq(mtx[i][1]-ybar)

    stdx = st_dev(stdx)
    stdy = st_dev(stdy)

    std = stdx*stdy

    a = cov[0][0] / sq(stdx)
    b = cov[0][1] / std
    c = cov[1][0] / std
    d = cov[1][1] / sq(stdy)

    return np.array([
        [a, b],
        [c, d]
    ])
