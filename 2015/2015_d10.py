#🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎅 Python 3.12.1 🎄


import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))
from tools import timer


data = "..." # your data 🥂


#🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄⛄

from functools import reduce
from itertools import groupby


@timer # [0.2013 sec]
def fun_part_1(data, n=40):
    look_and_say = lambda s, _: "".join(str(len([*g]))+k for k, g in groupby(s))
    repeat_and_get_len = lambda s, n, f: len(reduce(f, range(n), s))
    return repeat_and_get_len(data, n, look_and_say)


@timer # [_ sec]
def fun_part_1_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄🥳


@timer # [2.9738 sec]
def fun_part_2(data, n=50):
    look_and_say = lambda s, _: "".join(str(len([*g]))+k for k, g in groupby(s))
    repeat_and_get_len = lambda s, n, f: len(reduce(f, range(n), s))
    return repeat_and_get_len(data, n, look_and_say)


@timer # [_ sec]
def fun_part_2_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🧝
