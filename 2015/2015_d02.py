#🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎅 Python 3.12.1 🎄


import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))
from tools import timer


with open("2015_d02.txt") as f: # 🥂
    data = f.read().strip()


#🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄⛄

from itertools import starmap


@timer # [0.0011 sec]
def fun_part_1(data):
    lines = (line.split("x") for line in data.splitlines())
    lines = (sorted(map(int, line)) for line in lines)
    f = lambda L, W, H: 2 * (L * W + W * H + H * L) + L * W
    return sum(starmap(f, lines))


@timer # [_ sec]
def fun_part_1_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄🥳


@timer # [0.0009 sec]
def fun_part_2(data):
    lines = (line.split("x") for line in data.splitlines())
    lines = (sorted(map(int, line)) for line in lines)
    f = lambda L, W, H: 2 * (L + W) + W * H * L
    return sum(starmap(f, lines))


@timer # [_ sec]
def fun_part_2_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🧝
