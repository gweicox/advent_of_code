#🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎅 Python 3.12.1 🎄


import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))
from tools import timer


with open("2015_d05.txt") as f: # 🥂
    data = f.read().strip()


#🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄⛄

from itertools import pairwise
import re


@timer # [0.0018 sec]
def fun_part_1(data):
    lines = data.splitlines()

    a = lambda line: sum(x in "aeiou" for x in line) > 2
    b = lambda line: any(a == b for a, b in pairwise(line))
    c = lambda line: all(e not in line for e in ("ab", "cd", "pq", "xy"))

    f = lambda line: a(line) and b(line) and c(line)
    return sum(f(line) for line in lines)


@timer # [0.0019 sec]
def fun_part_1_kind_of_like_improved_or_not(data):
    lines = data.splitlines()

    a = lambda line: not not re.search(r'([aeiou].*){3}', line)
    b = lambda line: not not re.search(r'(.)\1', line)
    c = lambda line: not re.search(r'ab|cd|pq|xy', line)

    return sum([a(line) and b(line) and c(line) for line in lines])


#🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄🥳


@timer # [0.0029 sec]
def fun_part_2(data):
    lines = data.splitlines()

    a = lambda line: any(a + b in line[i+2:] for i, (a, b) in enumerate(pairwise(line)))
    b = lambda line: any(a == b for a, b in zip(line, line[2:]))

    f = lambda line: a(line) and b(line)
    return sum(f(line) for line in lines)


@timer # [0.0016 sec]
def fun_part_2_kind_of_like_improved_or_not(data):
    lines = data.splitlines()

    a = lambda line: not not re.search(r'(..).*\1', line)
    b = lambda line: not not re.search(r'(.).\1', line)

    return sum([a(line) and b(line) for line in lines])


#🎄❄🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🧝
