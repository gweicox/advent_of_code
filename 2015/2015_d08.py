#🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎅 Python 3.12.1 🎄


import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))
from tools import timer


with open("2015_d08.txt") as f: # 🥂
    data = f.read().strip()


#🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄⛄


@timer # [0.0018 sec]
def fun_part_1(data):
    table = data.splitlines()
    return sum(len(line) - len(eval(f"{line}")) for line in table)


@timer # [_ sec]
def fun_part_1_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄🥳


@timer # [0.0001 sec]
def fun_part_2(data):
    table = data.splitlines()
    return sum(line.count("\"") + line.count("\\") + 2 for line in table)


@timer # [_ sec]
def fun_part_2_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🧝
