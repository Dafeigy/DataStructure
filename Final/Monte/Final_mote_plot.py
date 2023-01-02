import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import random

random.seed(20221230)

def judge_distance(p1:list[int], p2:list[int], radius):
    '''
    判断p1 是否在以p2为圆心半径为radius的圆内
    '''
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 <= radius**2

def filter(origin_data:list[list[int]]):
    '''
    用Hashmap清洗重复的坐标
    '''
    return list({str(each):each for each in origin_data}.values())

if __name__ == "__main__":
    # PARAMS
    RADIUS = 5
    N = 5            # 圆个数


    int_list = [list(each) for each in list(itertools.product(range(0, 50), range(0, 50)))]
    circle_list = random.sample(int_list, N)
    filtered = filter(circle_list)
    x_data, y_data = zip(*filtered) 
    data = {"X":'x', "Y":'y'}
    x_data = list(x_data)
    y_data = list(y_data)
    
    plt.scatter(x=x_data, y=y_data, s = 5000, marker='o', alpha = 0.5)
    plt.show()


