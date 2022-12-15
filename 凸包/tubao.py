# trees 为测试数组
trees = [[2,2],[1,1],[2,0],[2,4],[3,3],[4,2]]


def tubao(trees) -> list[list[int]]:
    if len(trees) <4:
        return trees
    def judge_turn(p1:list[int], p2:list[int], p3:list[int]):
        '''
        用于计算选中的三个点是否有一种“左拐/逆时针的趋势”,本质是斜率的比较
        Args:
            points locations [x,y]
        Return:
            Bool for whether the curve has a cloack wise reverse tendency
        '''
        return (p2[0] - p1[0]) * (p3[1] - p2[1]) - (p2[1] - p1[1]) * (p3[0] - p2[0]) < 0
    # 先对列表坐标进行升序排序，优先排x，然后排y
    trees.sort()
    # queue 用于维护可以用于凸包的点
    # used 用于保存使用过的点
    queue = [0] # 因为已经排序过了，此时trees[0]或者trees[-1]对应的肯定是凸包上的点
    used = [False] * len(trees)

    # 下半部分的遍历
    n = len(trees)
    for i in range(1, n):
        while len(queue) > 1 and judge_turn(trees[queue[-2]], trees[queue[-1]], trees[i]):
            used[queue.pop()] = False
        used[i] = True
        queue.append(i)

    # 上半部分的遍历
    m = len(queue)
    for i in range(n - 2, -1, -1):
        if not used[i]:
            while len(queue) > m and judge_turn(trees[queue[-2]], trees[queue[-1]], trees[i]):
                used[queue.pop()] = False
            used[i] = True
            queue.append(i)
    
    # 弹出queue中最后一个元素，因为它重复保存了上/下部分的凸包点
    queue.pop()
    return [trees[i] for i in queue]

if __name__ == "__main__":
    result = tubao(trees)
    print(result)