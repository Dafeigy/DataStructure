def halton(b:int,N:int):
    '''
    Args:
        b: `PRIME` int
        N:  Sample num
    
    Return:
        seuqnce: list of N Halton Sequence
    '''
    n, d = 0, 1             # n,d 左右区间
    sequence = []
    for _ in range(1,N+1):  # 生成样本
        x = d - n           # 计算区间长度
        if x == 1:
            n = 1
            d *= b          # 扩大区间，避免四舍五入产生的问题
        else:
            y = d // b      # 扩大区间的倍率
            while x <= y:   
                y //= b     # 如果区间扩大倍率太大的话要将它转换到0，1这个范围内
            n = (b + 1) * y - x # 缩放区间
        sequence.append(n/d)
        # print(n/d)
    return sequence

if __name__ == '__main__':
    x = halton(2,100)
    print(x)
