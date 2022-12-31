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

# PARAMS
N = 10
gen_length = N
dmatrix = []
prob_mutate = .4
individuals_num = 60
epoch_num = 100

class Individual():

    def __init__(self, gene = None) -> None:
        '''
        个体类，包含个体的核心特征`gene`和计算适应度的功能。
        '''
        if gene is not None:
            self.gene = gene 
        else:
            temp = [_ for _ in range(gen_length)]
            random.shuffle(temp)
            self.gene = temp
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        '''
        适应度函数表示为
        $
        \\frac{1}{\sum_{i=1}^{N-1}d_{i,i+1}}
        $
        '''
        return 1/(sum([dmatrix[self.gene[i]][self.gene[i+1]] for i in range(gen_length-1)]) \
            + dmatrix[self.gene[-1]][self.gene[0]])

class GA():
    def __init__(self,dmatrix) -> None:
        '''
        GA算法，包含GA算法的核心操作方式。

        Args:
            dmatrix: `numpy.ndrray`.表示距离矩阵。
        '''
        self.dmatrix = dmatrix
        self.individuals = []
        self.results = []
        self.best_fiteness = []
        self.best = None
        

    def mutate(self,next_gen):
        '''
        子代进行变异操作，即将基因序列中的部分片段进行反转。
        Args:
            next_gene: list[list[int]], 若干整数列表（基因序列）组成的列表（子代合集）
        '''
        for each in next_gen:
            if random.random()<prob_mutate:
                prev_gene = each.gene.copy()
                start_index = random.randint(0,gen_length -2)
                end_index = random.randint(start_index, gen_length -1)
                mutate_gene = prev_gene[start_index:end_index]
                mutate_gene.reverse()
                each.gene = prev_gene[:start_index] + mutate_gene + prev_gene[end_index:]
        self.individuals += next_gen


    def cross(self):
        '''
        杂交，从某个Generation中的Individual中随机两两不重复组合作为父母，然后从父母的片段中筛选基因片段进行重组
        然后产生两个后代。

        Args：
            return list[Individual]
        '''
        random.shuffle(self.individuals)
        next_gen = []
        for i in range(0, individuals_num, 2):
            f_gene = self.individuals[i].gene.copy()    # Father Gene
            m_gene = self.individuals[i+1].gene.copy()  # Mother Gene
            # 使用Hashmap记录顺序的对应index
            f_hash = {v:k for k,v in enumerate(f_gene)}
            m_hash = {v:k for k,v in enumerate(m_gene)}
            # 交叉位置随机生成
            start_index = random.randint(0, gen_length-2)
            end_index = random.randint(start_index, gen_length-1) 
            # 交叉
            for j in range(start_index, end_index):
                vf,vm = f_gene[j], m_gene[j]
                pos_f, pos_m = f_hash[vm], m_hash[vf]
                f_gene[j], f_gene[pos_f] = f_gene[pos_f], f_gene[j]
                m_gene[j], m_gene[pos_m] = m_gene[pos_m], m_gene[j]
                # 更新Hashmap
                f_hash[vf], f_hash[vm] = pos_f, j
                m_hash[vf], m_hash[vm] = j, pos_m
            next_gen.append(Individual(f_gene))
            next_gen.append(Individual(m_gene))
        return next_gen

    def select_next_gen(self):
        '''
        锦标赛选择下一代。
        '''
        # Code from 
        group_num = 10  # 小组数
        group_size = 10  # 每小组人数
        group_winner = individuals_num // group_num  # 每小组获胜人数
        winners = []  # 锦标赛结果
        for i in range(group_num):
            group = []
            for j in range(group_size):
                # 随机组成小组
                player = random.choice(self.individuals)
                player = Individual(player.gene)
                group.append(player)
            group = sorted(group,key=lambda x:x.gene)
            # 取出获胜者
            winners += group[:group_winner]
        self.individuals = winners

    def step(self):
        '''
        迭代过程。
        '''
        # 杂交
        next_gen = self.cross()
        # 变异
        self.mutate(next_gen)
        # 优胜劣汰
        self.select_next_gen()

        for individual in self.individuals:
            if individual.fitness > self.best.fitness:
                self.best = individual

    def train(self, epoch_num):
        '''
        Args:
            INPUT: epoch_num: 训练的轮数
            OUTPUT:
                self.results: 最优解
                self.best_fiteness: 适应度历史
        '''
        self.individuals = [ Individual() for _ in range(individuals_num)]
        self.best = self.individuals[0]
        for epoch in range(epoch_num):
            self.step()
            result = self.best.gene.copy()
            result.append(result[0])

            self.results.append(result)
            self.best_fiteness.append(self.best.fitness)
        
        return self.results, self.best_fiteness

if __name__ == "__main__":
    '''
    1/(sum([dmatrix[self.gene[i]][self.gene[i+1]] for i in range(gen_length-1)]) \
            + dmatrix[self.gene[-1]][self.gene[0]])
    '''
    

        
            








