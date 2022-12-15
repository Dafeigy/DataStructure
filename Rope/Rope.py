# 我的博客有代码备份https://cybercolyce.cn/2022/11/12/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84-Rope/
# 叶节点用Str表示，其左右子树指向None代表已经到底了
# 也可以用[Str]进行Rope构建
# 递归实现，任意组合都可以是一个Rope

class Rope(object):
    def __init__(self, data='') -> None:
        if isinstance(data,list):
            if len(data) == 0:
                self.__init__()
            elif len(data) == 1:
                self.__init__(data[0])
            else:
                idiv = len(data)//2 + (len(data)%2>0)

                self.left = Rope(data[:idiv])
                self.right = Rope(data[idiv:])
                self.data = ''
                self.length = self.left.length + self.right.length
        
        elif isinstance(data,str):
            self.left = None
            self.right = None
            self.data = data
            self.length = len(data)

        else:
            raise TypeError('只能使用`Str`或`List:[Str]`作为Rope的传入数据')
        
        self.current = self
    
    def __add__(self, inputdata):
        if isinstance(inputdata, str):
            inputdata = Rope(inputdata)
        
        tmp = Rope()
        tmp.left = self
        tmp.right = inputdata
        tmp.length = tmp.left.length + tmp.right.length
        tmp.current = self
        return tmp
    
    def __len__(self):
        # 非叶节点长度
        if self.left and self.right:
            return len(self.left) + len(self.right)
        # 叶节点长度
        else:
            return(len(self.data))

    def __getitem__(self, index):
        if isinstance(index, int):
            if self.left and self.right:
                if index < -self.right.length:
                    subindex = index + self.right.length
                elif index >= self.left.length:
                    subindex = index - self.left.length
                else:
                    subindex = index

                if index < -self.right.length or 0 <= index < self.left.length:
                    return self.left[subindex]
                else:
                    return self.right[subindex]
            else:
                return Rope(self.data[index])

        elif isinstance(index, slice):
            if self.left and self.right:
                start = index.start
                if index.start is None:
                    if index.step is None or index.step > 0:
                        head = self.left
                    else:
                        head = self.right
                elif (index.start < -self.right.length or
                        0 <= index.start < self.left.length):
                    head = self.left
                    if index.start and index.start < -self.right.length:
                        start += self.right.length
                else:
                    head = self.right
                    if index.start and index.start >= self.left.length:
                        start -= self.left.length

                stop = index.stop
                if index.step is None or index.step > 0:
                    if (index.stop is None or
                            -self.right.length <= index.stop < 0 or
                            index.stop > self.left.length):
                        tail = self.right
                        if index.stop and index.stop > self.left.length:
                            stop -= self.left.length
                    else:
                        if head == self.right:
                            tail = self.right
                            stop = 0
                        else:
                            tail = self.left
                            if index.stop < -self.right.length:
                                stop += self.right.length
                else:
                    if (index.stop is None or
                            index.stop < (-self.right.length - 1) or
                            0 <= index.stop < self.left.length):
                        tail = self.left
                        if index.stop and index.stop < (-self.right.length - 1):
                            stop += self.right.length
                    else:
                        if head == self.left:
                            tail = self.left
                            stop = -1   # Or self.left.length - 1 ?
                        else:
                            tail = self.right
                            if index.stop >= self.left.length:
                                stop -= self.left.length

                # Construct the rope
                if head == tail:
                    return head[start:stop:index.step]
                else:
                    if not index.step:
                        offset = None
                    elif index.step > 0:
                        if start is None:
                            delta = -head.length
                        elif start >= 0:
                            delta = start - head.length
                        else:
                            delta = max(index.start, -self.length) + tail.length

                        offset = delta % index.step
                        if offset == 0:
                            offset = None
                    else:
                        if start is None:
                            offset = index.step + (head.length - 1) % (-index.step)
                        elif start >= 0:
                            offset = index.step + min(start, head.length - 1) % (-index.step)
                        else:
                            offset = index.step + (start + head.length) % (-index.step)

                    if not tail[offset:stop:index.step]:
                        return head[start::index.step]
                    else:
                        return head[start::index.step] + tail[offset:stop:index.step]
            else:
                return Rope(self.data[index])

    def __repr__(self):
        if self.left and self.right:
            return '{}{} + {}{}'.format('(' if self.left else '',
                                        self.left.__repr__(),
                                        self.right.__repr__(),
                                        ')' if self.right else '')
        else:
            return "\033[1;37;42mRope ['{}']\033[0m".format(self.data)

    def split(self, index):
        if isinstance(index, int):
            if self.left and self.right:
                    if index < -self.right.length:
                        subindex = index + self.right.length
                    elif index >= self.left.length:
                        subindex = index - self.left.length
                    else:
                        subindex = index

                    if index < -self.right.length or 0 <= index < self.left.length:
                        return self.left[:subindex], self.left[subindex:]
                    else:
                        return self.right[:subindex], self.right[subindex:]
            else:
                return Rope(self.data[:index]), Rope(self.data[index:])
        else:
            raise TypeError("`index`必须为`Int`类型")

if __name__ == "__main__":
    a = Rope('hello')
    b = Rope('world')
    c = Rope(['I ', "don't", "know"])

    r = a + b
    print(c)
    print(r)
    print(r[6])
    print(r.split(3))
    
# ((Rope ['I '] + Rope ['don't']) + Rope ['know'])
# (Rope ['hello'] + Rope ['world'])
# Rope ['o']
# (Rope ['hel'], Rope ['lo'])