#🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎅 Python 3.12.1 🎄


import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))
from tools import timer


data = "..." # your data 🥂


#🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄⛄

import numpy as np


@timer # [2.8024 sec]
def fun_part_1(data):
    N = int(data)
    L = 10**6
    arr = [10] * L

    for i in range(2, L):
        curr = i * 10
        for j in range(i, L, i):
            arr[j] += curr

    for indx, e in enumerate(arr):
        if e >= N:
            return indx


@timer # [0.7681 sec]
def fun_part_1_kind_of_like_improved_or_not(data):
    N = int(data)
    L = 10**6
    arr = np.arange(L) * 10

    for i in range(1, L//2):
        arr[i+i::i] += i * 10

    return np.argmax(arr > N)


#🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄🥳


@timer # [1.0389 sec]
def fun_part_2(data):
    N = int(data)
    L = 10**6
    arr = [0] * L

    for i in range(1, L):
        curr = i * 11
        for j in range(i, min(L, i*50+1), i):
            arr[j] += curr

    for indx, e in enumerate(arr):
        if e >= N:
            return indx


@timer # [0.7296 sec]
def fun_part_2_kind_of_like_improved_or_not(data):
    N = int(data)
    L = 10**6
    arr = np.arange(L) * 11

    for i in range(2, L//2):
        arr[i+i:i*50+1:i] += i * 11

    return np.argmax(arr > N)


#🎄❄🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🧝
