from tubao import tubao
import time
import itertools
import random
import matplotlib.pyplot as plt
from tqdm import tqdm
import seaborn as sns
import pandas as pd


random.seed(20221215)
plt.rcParams['figure.dpi'] = 75  # 图形分辨率
sns.set_theme(style='darkgrid')  # 图形主题

# N = [i for i in range(1000, 10001)]
# random_list = [list(each) for each in list(itertools.product(range(1, 101), range(1, 101)))]



if __name__ == '__main__':
    
    # x_data = pd.Series(N)
    # time_list = []

    # for n in tqdm(N):
    #     temp = random.sample(random_list,N[n-1000]) # 1000是起始点
    #     start = time.time()
    #     res = tubao(temp)
    #     end = time.time() - start
    #     time_list.append(end)

    # y_data = pd.Series(time_list)
    # data = pd.DataFrame()
    # data['N'] = x_data
    # data['Time'] = y_data
    # data.to_csv('data.csv', index=False)
    data = pd.read_csv('data.csv')
    sns.lineplot(data=data, x='N', y = 'Time')
    plt.show()
    plt.savefig("result.png")