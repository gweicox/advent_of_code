#🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎅 Python 3.12.1 🎄


import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))
from tools import timer


with open("2015_d15.txt") as f: # 🥂
    data = f.read().strip()


#🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄⛄

from math import prod
from re import findall


@timer # [0.1582 sec]
def fun_part_1(data):
    table = [[*map(int, findall(r"-?\d+", line))] for line in data.splitlines()]
    table_T = [*zip(*table)][:-1] # transpose ignoring calories 
    max_prod = 0

    for x in range(101):
        for y in range(100-x):
            for z in range(100-x-y):
                q = 100-x-y-z
                curr = prod([max(0, a*x + b*y + c*z + d*q) for a, b, c, d in table_T])
                max_prod = max(max_prod, curr)

    return max_prod


@timer # [_ sec]
def fun_part_1_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄🥳


@timer # [0.0991 sec]
def fun_part_2(data):
    table = [[*map(int, findall(r"-?\d+", line))] for line in data.splitlines()]
    table_T = [*zip(*table)]
    calories = table_T.pop()
    max_prod = 0

    for x in range(101):
        for y in range(100-x):
            for z in range(100-x-y):
                q = 100-x-y-z
                if sum(a * b for a, b in zip(calories, (x, y, z, q))) == 500:
                    curr = prod([max(0, a*x + b*y + c*z + d*q) for a, b, c, d in table_T])
                    max_prod = max(max_prod, curr)

    return max_prod


@timer # [_ sec]
def fun_part_2_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🧝
