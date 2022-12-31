import random
import itertools
import numpy as np
import math


random.seed(20221231)

def generate_cities(N):
    '''
    生成N个城市
    '''
    random_list = list(itertools.product(range(1, N), range(1, N)))
    return random.sample(random_list, N)

def calculate_distance(p1,p2):
    '''
    计算点之间的距离的平方
    '''
    return sum([(x-y)**2 for x,y in zip(p1,p2)])

def generate_dmatrix(cities:list[list[int]]):
    N = len(cities)
    print(N)
    dmatrix = np.zeros([N,N])
    for i in range(N):
        for j in range(i+1,N):
            temp = np.array(cities[i]) - np.array(cities[j])
            dmatrix[i, j] = np.dot(temp, temp)
            dmatrix[j, i] = dmatrix[i, j]
    return dmatrix

def generate_dmatrix_fromlist(cities):
    N = len(cities)
    dmatrix = [[0.] * N for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            dmatrix[i][j] = calculate_distance(cities[i],cities[j])
            dmatrix[j][i] = dmatrix[i][j]
    return dmatrix


if __name__ == '__main__':
    random.seed(20221231)
    cities = generate_cities(10)
    dmatrix = generate_dmatrix_fromlist(cities)
    print(cities)
    print(dmatrix)
    '''
    [(2, 6), (6, 4), (7, 9), (1, 3), (9, 9), (4, 7), (1, 5), (2, 9), (9, 3), (3, 4)]

    [[  0.  20.  34.  10.  58.   5.   2.   9.  58.   5.]
    [ 20.   0.  26.  26.  34.  13.  26.  41.  10.   9.]
    [ 34.  26.   0.  72.   4.  13.  52.  25.  40.  41.]
    [ 10.  26.  72.   0. 100.  25.   4.  37.  64.   5.]
    [ 58.  34.   4. 100.   0.  29.  80.  49.  36.  61.]
    [  5.  13.  13.  25.  29.   0.  13.   8.  41.  10.]
    [  2.  26.  52.   4.  80.  13.   0.  17.  68.   5.]
    [  9.  41.  25.  37.  49.   8.  17.   0.  85.  26.]
    [ 58.  10.  40.  64.  36.  41.  68.  85.   0.  37.]
    [  5.   9.  41.   5.  61.  10.   5.  26.  37.   0.]]
    '''