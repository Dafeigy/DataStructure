import random
import itertools


def judge_distance(p1:list[int], p2:list[int], radius):
    '''
    判断p1 是否在以p2为圆心半径为radius的圆内
    为了方便生成圆心的坐标均为整数
    '''
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 <= radius**2

def filter(origin_data:list[list[int]]):
    '''
    用Hashmap清洗重复的坐标
    '''
    return list({str(each):each for each in origin_data}.values())

def rect(origin:list[int],radius:int):
    '''
    用来返回最小外接矩形的顶点坐标
    返回x_min, y_min, x_max, y_max
    '''
    y_data = [each[1] for each in origin]
    x_data = [each[0] for each in origin]
    # return min(x_data), min(y_data), max(x_data), max(y_data)
    return min(x_data)-radius, min(y_data)-radius, max(x_data)+radius, max(y_data)+radius

def generate_sample(N_sample,x_min,y_min,x_max, y_max):
    '''
    生成矩形区域的采样点集合
    '''
    return [[random.uniform(x_min, x_max),random.uniform(y_min, y_max)] for _ in range(N_sample)]

if __name__ == '__main__':
    # PARARMS
    RADIUS = 5
    N = 5            # 圆个数
    N_sample = 10 # 采样点数
    random.seed(20221230)   # 随机种子 我开始写的日期



    #########################################
    # 产生圆心
    int_list = [list(each) for each in list(itertools.product(range(0, 50), range(0, 50)))]
    circle_list = random.sample(int_list, N)
    
    # 数据清洗
    filtered = filter(circle_list)

    # 外接矩形
    x_min, y_min, x_max, y_max = rect(filtered,RADIUS)

    # 生成采样点
    sample_list = generate_sample(N_sample, x_min, y_min, x_max, y_max)

    # 矩形面积
    S_rect = (x_max-x_min) * (y_max - y_min)

    # 初始计数
    count = 0

    # 遍历Hashmap
    for sample in sample_list:
        for circle in circle_list:
            if judge_distance(sample, circle, RADIUS):
                count += 1
                break
    
    # Final
    print(count/N_sample * S_rect)
    
