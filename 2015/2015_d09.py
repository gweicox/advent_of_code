#🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎅 Python 3.12.1 🎄


import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))
from tools import timer


with open("2015_d09.txt") as f: # 🥂
    data = f.read().strip()


#🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄⛄

from itertools import permutations


@timer # [0.0423 sec]
def fun_part_1(data):
    routes = [line.split() for line in data.splitlines()]
    G, locs = {}, set()

    for a, _, b, _, dist in routes:
        G[(a, b)] = G[(b, a)] = int(dist)
        locs |= {a, b}

    curr_min = float("inf")

    for route in permutations(locs):
        acc = 0
        for a, b in zip(route, route[1:]):
            acc += G[(a, b)]
        curr_min = min(curr_min, acc)

    return curr_min


@timer # [_ sec]
def fun_part_1_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄🥳


@timer # [0.0429 sec]
def fun_part_2(data):
    routes = [line.split() for line in data.splitlines()]
    G, locs = {}, set()

    for a, _, b, _, dist in routes:
        G[(a, b)] = G[(b, a)] = int(dist)
        locs |= {a, b}

    curr_max = 0

    for route in permutations(locs):
        acc = 0
        for a, b in zip(route, route[1:]):
            acc += G[(a, b)]
        curr_max = max(curr_max, acc)

    return curr_max


@timer # [_ sec]
def fun_part_2_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🧝
