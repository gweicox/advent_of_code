#🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎅 Python 3.12.1 🎄


import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))
from tools import timer


with open("20xx_dxx.txt") as f: # 🥂
    data = f.read().strip()


#🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄⛄


@timer # [_ sec]
def fun_part_1(data):
    pass


@timer # [_ sec]
def fun_part_1_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄🥳


@timer # [_ sec]
def fun_part_2(data):
    pass


@timer # [_ sec]
def fun_part_2_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🧝

print(fun_part_1(data))
print(fun_part_1_kind_of_like_improved_or_not(data))

print(fun_part_2(data))
print(fun_part_2_kind_of_like_improved_or_not(data))
