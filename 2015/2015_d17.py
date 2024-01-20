#🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎅 Python 3.12.1 🎄


import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))
from tools import timer


with open("2015_d17.txt") as f: # 🥂
    data = f.read().strip()


#🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄⛄

from itertools import combinations


@timer # [0.1393 sec]
def fun_part_1(data, total_volume=150):
    containers = [int(line) for line in data.splitlines()]
    acc = 0
    for n in range(1, len(containers)+1):
        for combination in combinations(containers, n):
            if sum(combination) == total_volume:
                acc += 1
    return acc


@timer # [0.0001 sec]
def fun_part_1_kind_of_like_improved_or_not(data, V=150):
    containers = [int(line) for line in data.splitlines()]

    dp = [1] + [0] * V

    for curr_num in containers:
        for next_num in range(V, curr_num-1, -1):
            dp[next_num] += dp[next_num - curr_num]

    return dp[V]


#🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄🥳


@timer # [0.0007 sec]
def fun_part_2(data, total_volume=150):
    containers = [int(line) for line in data.splitlines()]
    acc = 0
    for n in range(1, len(containers)+1):
        for combination in combinations(containers, n):
            if sum(combination) == total_volume:
                acc += 1
        if acc:
            return acc


@timer # [_ sec]
def fun_part_2_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🧝
