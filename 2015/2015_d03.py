#🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎅 Python 3.12.1 🎄


import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))
from tools import timer


with open("2015_d03.txt") as f: # 🥂
    data = f.read().strip()


#🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄⛄

from itertools import accumulate as acc


@timer # [0.0014 sec]
def fun_part_1(data):
    dirs = {"^": 1j, "<": -1, "v": -1j, ">": 1}
    f = lambda last, curr: last + dirs[curr]
    uniq_houses = set(acc(data, f, initial=0))
    return len(uniq_houses)


@timer # [_ sec]
def fun_part_1_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄🥳


@timer # [0.0016 sec]
def fun_part_2(data):
    dirs = {"^": 1j, "<": -1, "v": -1j, ">": 1}
    f = lambda last, curr: last + dirs[curr]
    uniq_houses = set((*acc(data[::2],  f, initial=0),
                       *acc(data[1::2], f, initial=0)))
    return len(uniq_houses)


@timer # [_ sec]
def fun_part_2_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🧝
