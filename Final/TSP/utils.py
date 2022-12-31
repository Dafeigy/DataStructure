import random
import itertools
import numpy as np
import math


def generate_cities(N):
    '''
    生成N个城市。
    '''
    random_list = list(itertools.product(range(1, N), range(1, N)))
    return random.sample(random_list, N)

def calculate_distance(p1,p2):
    '''
    计算点之间的距离的平方，不开根号减少计算量。
    '''
    return sum([(x-y)**2 for x,y in zip(p1,p2)])


def generate_dmatrix(cities:list[list[int]] or list[list[float]]):
    '''
    生成距离矩阵。
    '''
    N = len(cities)
    dmatrix = [[0.] * N for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            dmatrix[i][j] = calculate_distance(cities[i],cities[j])
            dmatrix[j][i] = dmatrix[i][j]
    return dmatrix

def generate_hex(p:list[list[int or float]], r:int or float):
    '''
    产生六边形坐标。
    Args:
        p: 六边形中点坐标。
        r: 六边形边长
    '''
    x,y = p[0],p[1]
    p1 = [x - 0.5*r, y - 0.5 * math.sqrt(3) * r]
    p2 = [x - 1*r, y]
    p3 = [x - 0.5*r, y + 0.5 * math.sqrt(3)* r]
    p4 = [x + 0.5*r, y + 0.5 * math.sqrt(3)* r]
    p5 = [x + 1*r, y ]
    p6 = [x + 0.5*r, y - 0.5 * math.sqrt(3)* r]
    return p1,p2,p3,p4,p5,p6


if __name__ == '__main__':
    random.seed(20221231)
    cities = generate_cities(10)
    dmatrix = generate_dmatrix(cities)
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