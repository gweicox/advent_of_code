#🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎅 Python 3.12.1 🎄


import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))
from tools import timer


with open("2015_d01.txt") as f: # 🥂
    data = f.read().strip()


#🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄⛄


@timer # [0.0003 sec]
def fun_part_1(data):
    return sum((-1, 1)[symbol == "("] for symbol in data)


@timer # [0.0001 sec]
def fun_part_1_kind_of_like_improved_or_not(data):
    return data.count("(") - data.count(")")


#🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄🥳


@timer # [0.0001 sec]
def fun_part_2(data):
    curr_floor = 0
    for indx, symbol in enumerate(data, 1):
        curr_floor += (-1, 1)[symbol == "("]
        if curr_floor == -1:
            return indx


@timer # [0.0005 sec]
def fun_part_2_kind_of_like_improved_or_not(data):
    from itertools import accumulate as acc
    return [*acc((-1, 1)[x=="("] for x in data)].index(-1) + 1


#🎄❄🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🧝
