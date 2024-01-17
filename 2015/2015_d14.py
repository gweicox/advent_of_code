#🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎅 Python 3.12.1 🎄


import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))
from tools import timer


with open("2015_d14.txt") as f: # 🥂
    data = f.read().strip()


#🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄⛄

from re import findall


@timer # [0.0001 sec]
def fun_part_1(data, time=2503):
    table = (map(int, findall(r"\d+", line)) for line in data.splitlines())

    def get_distance(v, t1, t2, time):
        return v * (time // (t1 + t2) * t1 + min(time % (t1 + t2), t1))

    return max(get_distance(*row, time) for row in table)


@timer # [_ sec]
def fun_part_1_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄🥳


@timer # [0.0096 sec]
def fun_part_2(data, time=2503):
    table = [[*map(int, findall(r"\d+", line))] for line in data.splitlines()]

    res = [0] * len(table)

    def get_distance(v, t1, t2, time):
        return v * (time // (t1 + t2) * t1 + min(time % (t1 + t2), t1))

    def get_awards(table, time):
        curr = [get_distance(*row, time) for row in table]
        curr_max = max(curr)
        return [x == curr_max for x in curr]

    for t in range(1, time+1):
        res = [a + b for a, b in zip(res, get_awards(table, t))]

    return max(res)


@timer # [_ sec]
def fun_part_2_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🧝
