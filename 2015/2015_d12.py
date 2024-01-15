#🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎅 Python 3.12.1 🎄


import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))
from tools import timer


with open("2015_d12.txt") as f: # 🥂
    data = f.read().strip()


#🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄⛄

from re import findall


@timer # [0.0018 sec]
def fun_part_1(data):
    return sum(map(int, findall(r"-?\d+", data)))


@timer # [_ sec]
def fun_part_1_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄🥳

from json import loads


@timer # [0.0015 sec]
def fun_part_2(data):

    def sum_allowed_values(item):
        if type(item) == int: return int(item)
        if type(item) == str: return 0
        if type(item) == dict:
            values = item.values()
            return 0 if "red" in values else sum_allowed_values(values)
        return sum(map(sum_allowed_values, item))

    return sum_allowed_values(loads(data))


@timer # [0.0019 sec]
def fun_part_2_kind_of_like_improved_or_not(data):
    drop_red = lambda dct: (dct, "")["red" in dct.values()]
    new_data = str(loads(data, object_hook=drop_red))
    return sum(map(int, findall(r"-?\d+", new_data)))


#🎄❄🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🧝
