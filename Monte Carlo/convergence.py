import matplotlib.pyplot as plt
import pandas as pd
import math
import seaborn as sns
from tqdm import tqdm
import chaospy

uniform_cube = chaospy.J(chaospy.Uniform(0, 1), chaospy.Uniform(0, 1))

if __name__ == '__main__':

    sample_min = 10
    sample_max = 1000
    err_random_list = []
    err_quasi_list  = []

    for sample_num in tqdm(range(sample_min, sample_max+1)):
        random_samples = uniform_cube.sample(sample_num, rule="random", seed=20221215)
        halton_samples = uniform_cube.sample(sample_num, rule="halton", seed=20221215)
        x_random,y_random = random_samples
        x_quasi, y_quasi = halton_samples


        count_random = 0
        count_quasi = 0
        for _ in range(sample_num):
            count_random += 1 if x_random[_]**2 + y_random[_]**2 <= 1 else 0
            count_quasi += 1 if x_quasi[_]**2 + y_quasi[_]**2 <= 1 else 0
        err_random = abs(math.pi - 4*count_random/sample_num)
        err_quasi = abs(math.pi - 4*count_quasi/sample_num)
        err_random_list.append(err_random)
        err_quasi_list.append(err_quasi)

    df = pd.DataFrame({
        'Basic MC':err_random_list,
        'Quasi MC':err_quasi_list
    })


    sns.lineplot(df)
    plt.show()


