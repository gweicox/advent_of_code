#🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎅 Python 3.12.1 🎄


import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))
from tools import timer


with open("2015_d13.txt") as f: # 🥂
    data = f.read().strip()


#🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄⛄

from itertools import permutations


@timer # [0.0750 sec]
def fun_part_1(data):
    table = [line.replace("lose ", "-") for line in data.splitlines()]
    table = [line.replace("gain ", "").replace(".", "").split() for line in table]
    table = {(row[0], row[-1]): int(row[2]) for row in table}
    persons = {pair[0] for pair in table}

    perm_e = lambda it: {min(x, x[::-1]) for x in permutations(it)}
    pair_e = lambda it: [*zip(it, [*it[1:]] + [it[0]])]
    get_happiness = lambda pairs: sum(table[pair] + table[pair[::-1]] for pair in pairs)

    return max(get_happiness(pair_e(arrangement)) for arrangement in perm_e(persons))


@timer # [_ sec]
def fun_part_1_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄🥳


@timer # [0.7687 sec]
def fun_part_2(data):
    table = [line.replace("lose ", "-") for line in data.splitlines()]
    table = [line.replace("gain ", "").replace(".", "").split() for line in table]
    table = {(row[0], row[-1]): int(row[2]) for row in table}
    persons = {pair[0] for pair in table}

    me_pers = {("me", x): 0 for x in persons}
    pers_me = {(x, "me"): 0 for x in persons}
    table = {**table, **me_pers, **pers_me}
    persons = persons | {"me"}

    perm_e = lambda it: {min(x, x[::-1]) for x in permutations(it)}
    pair_e = lambda it: [*zip(it, [*it[1:]] + [it[0]])]
    get_happiness = lambda pairs: sum(table[pair] + table[pair[::-1]] for pair in pairs)

    return max(get_happiness(pair_e(arrangement)) for arrangement in perm_e(persons))


@timer # [_ sec]
def fun_part_2_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🧝
