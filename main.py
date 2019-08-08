#encode:utf-8
import sys
import re
from collections import Counter


def hashtag(h='in.txt'):
    f = open(h, 'r')
    file = f.readlines()
    f.close()
    S = [re.findall(r'#\w+', y) for y in file]
    mass_10 = []
    z = Counter()
    for i in S:
        E = Counter(i)
        z += E
    z1 = Z.most_common(10)
    for k, v in z1:
        mass_10.append(k)  # массив с 10 значимыми хэштегами

    slov_hashtag = {}  # словарь с хэштегами
    for i in mass_10:
        g = Counter()
        for k in file:
            q1 = re.sub(r'\#[A-Za-z]+', '', k)
            if i in k:
                k1 = re.findall(r'\b[a-zA-Z]+', q1)
                f = Counter(k1)
                g += f
            else:
                continue
        g1 = g.most_common(5)
        n = []
        for k, v in g1:
            n.append(k)
        slov_hashtag[i] = n
    return sys.stdout.write(str(mass_10) + '\n' + str(slov_hashtag))

hashtag()