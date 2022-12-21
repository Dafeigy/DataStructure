import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math
from tqdm import tqdm



# x = np.linspace(0,1,100)
# y = [math.sqrt(1-x[i]**2) for i in range(len(x))]

# ax=plt.subplots(1,1)[1]
# ax.plot(x,y)
random.seed(20221215)
init = 10
size = 10000
err_list = []

for i in tqdm(range(10, size+1)):
    count = 0
    for _ in range(i):
        count += 1 if random.random()**2 + random.random()**2 <= 1 else 0
    err = abs(math.pi - 4*count/size)
    err_list.append(err)
    
sns.lineplot(err_list)
plt.show()
# x,y = zip(*points)
# plt.scatter(x,y,s=1) #绘制点
# plt.xlim(0,1)
# plt.ylim(0,1)
# plt.show()

