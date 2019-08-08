#encode:utf-8
import sys
import re
from collections import Counter


def hashtag(h = 'in.txt'):
    f = open(h, 'r')
    l = f.readlines()
    f.close()
    # перебором в массиве строк сделать findall
    S = []
    for y in l:
        T = re.findall(r'#\w+', y)
        S.append(T)
    a = []
    Z = Counter()
    for i in S:
        E = Counter(i)
        Z += E
    Z1 = Z.most_common(10)
    for k,v in Z1:
        a.append(k) # массив с 10 значимыми хэштегами
        #  словарь с массивами значимых слов
    r = {}

       # массив для значимых слов
    for i in a:
        G = Counter()
        for k in l:
            q1 = re.sub(r'\#[A-Za-z]+', '', k)
            if i in k:
                k1 = re.findall(r'\b[a-zA-Z]+', q1)
                f = Counter(k1)
                G += f
            else:
                continue
        G1 = G.most_common(5)
        n = []
        for k,v in G1:
            n.append(k)
        r[i] = n
    return sys.stdout.write(str(a) + '\n' + str(r))

hashtag()