


import math
from random import random


def basic_sigmoid(x):
 s = 1 / (1 + math.exp(-x))
 return s




print(ord("你"))
print(ord("1"))
print(ord("2"))
print(ord(" "))

ss = ["select a from db_ysb_order"
, "23423423"
, "223434"
, "5657"
,"778787989855345334dfa我们都是中国人"
, "select a from 223434safdf fdafd我们都是外国人 "
,"223434 om y sdfo ",
"9086"]

def getvector(str):
    arr = []
    for c in str:
        arr.append(ord(c))
    return arr


def convert(v, d):
    l = len(v)
    n = int(l / d)
    if(l % d != 0):
        n = int(l/d)+1
        for i in range(0, n - l % n):
            v.append(0)
    for i in range(0,d * n - len(v)):
        v.append(0)
    return [v[i:i + n] for i in range(0, len(v), n)]

def degree(str, d):
    arr2 = []
    v = getvector(str)
    m = convert(v, d)
    arr = []
    for l in m:
        sum = 0
        for val in l:
            sum += val
        arr.append(sum)
    for i in arr:
        arr2.append(math.log(i+1))
    return arr2

def distance(v1, v2):
    sum = 0.0
    for i in range(0, len(v1)):
        sum += math.pow(v1[i] - v2[i],2)
    return sum


def avg(v1, v2):
    v3 = []
    for i in range(0, len(v1)):
        v3.append((v1[i] + v2[i]) / 2)
    return v3

maxd = 10
k = 3

for d in range(1, maxd):
    vs = []
    for s in ss:
        vs.append({"v":degree(s, d)})

    # for v in vs:
    #     print(v)

    maxv = []
    for i in range(0, d):
        maxv.append(float("-inf"))

    for v in vs:
        for i in range(0, d):
            maxv[i] = max(maxv[i], v["v"][i])
            
    minv = []
    for i in range(0, d):
        minv.append(float("inf"))

    for v in vs:
        for i in range(0, d):
            minv[i] = min(minv[i], v["v"][i])

    # print(maxv)
    # print(minv)

    vks = []
    for i in range(0, k):
        vk = []
        for j in range(0,d):
            vk.append(minv[j] + random() *( maxv[j] - minv[j]))
        vks.append({"v":vk})

    e = 0
    while(e < 100):
        for v in vs:
            minvk = None
            minvkd = float("inf")
            for vk in vks:
                dist = distance(v["v"], vk["v"])
                if minvkd > dist:
                    minvkd = dist
                    minvk = vk
            v["c"] = minvk

        for vk in vks:
            com = vk["v"]
            for v in vs:
                if vk == v["c"]:
                    com = avg(com, v["v"])
            vk["v"] = com

        # print("\n")
        # for vk in vks:
        #     print(vk)
        e += 1

    # valid
    sumv = []
    sum = 0
    for v in vs:
        sum += distance(v["v"], v["c"]["v"])

    sumcomdist = 0
    for vk in vks:
        for vk2 in vks:
            if vk != vk2:
                sumcomdist += distance(vk["v"], vk2["v"])
    print(sumcomdist/sum)

    # for v in vs:
    #     print(v)

