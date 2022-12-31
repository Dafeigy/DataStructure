import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import random
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

if __name__ == "__main__":
    p1 = [6,8]
    p2 = [3,4]
    print(calculate_distance(p1,p2))
