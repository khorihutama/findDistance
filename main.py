import euclidean as eu
import correlation as col
import numpy as np

file = open( "data.txt" )

x = []
for line in file.readlines():
    y = [value for value in line.split()]
    x.append(y)

file.close()
# print(x)

mtx = np.array(x).astype(np.float)
# print(mtx)

# menghitung rata-rata x dan y

xSum = 0
ySum = 0
for i in range(len(mtx)):
    xSum += mtx[i][0]
    ySum += mtx[i][1]

xAvg = xSum/len(mtx)
yAvg = ySum/len(mtx)

# print(xAvg)
# print(yAvg)

# menghitung matrix covariance


def covariance(x, y, xbar, ybar):
    return (x-float(xbar))*(y-float(ybar))

# memanggil fungsi covariance

a = 0
b = 0
c = 0

for i in range(len(mtx)):
    a += covariance(float(x[i][0]), float(x[i][0]), xAvg, xAvg)
    b += covariance(float(x[i][0]), float(x[i][1]), xAvg, yAvg)
    c += covariance(float(x[i][1]), float(x[i][1]), yAvg, yAvg)

a = (a/len(mtx))
b = (b/(len(mtx)-1))
c = (c/len(mtx))

cov = np.array([[a, b], [b, c]])

print('Matrix covariance :')
print(cov)
print()
print('Matrix correlation :')
print(col.corr(cov, xAvg, yAvg, mtx))

# inversing matrix
try:
    inv = np.linalg.inv(cov)
except np.linalg.LinAlgError:
    # Not invertible. Skip this one.
    pass
else:
    # continue with what you were doing
    # print('Matrix inverse : \n', inverse)
    print()
while(True):
    arr = 0
    euclid = 0
    print()
    print('Data 1 :')
    p = float(input('\tFeature no 1 : '))
    q = float(input('\tFeature no 2 : '))
    print('Data 2 : ')
    p1 = float(input('\tFeature no 1 : '))
    q1 = float(input('\tFeature no 2 : '))

    pq = np.array([p, q])
    pq1 = np.array([p1, q1])

    arr = np.subtract(pq, pq1)
    euclid = eu.calc_euclid(pq, pq1)

    print('Euclidean distance   :\n', euclid)
    print('Mahalanobis distance :\n', np.matmul(np.matmul(arr.transpose(), inv), arr))
