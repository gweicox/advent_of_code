#🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎅 Python 3.12.1 🎄


import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))
from tools import timer


with open("2015_d06.txt") as f: # 🥂
    data = f.read().strip()


#🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄⛄

import numpy as np
import re


@timer # [0.0329 sec]
def fun_part_1(data):

    def parse(line):
        line = line.replace("turn off ", "0,").replace("turn on ", "1,")
        line = line.replace("toggle ", "-1,").replace(" through ", ",")
        return [*map(int, line.split(","))]

    def toggle(grid, instruction, coords):
        a, b, c, d = coords
        if instruction ==  0: grid[a:c+1, b:d+1] = 0
        if instruction ==  1: grid[a:c+1, b:d+1] = 1
        if instruction == -1: grid[a:c+1, b:d+1] = 1 - grid[a:c+1, b:d+1]

    instructions = [*map(parse, data.splitlines())]
    grid = np.zeros((1000, 1000), int)

    for instruction, a, b, c, d in instructions:
        toggle(grid, instruction, (a, b, c, d))

    return grid.sum()


@timer # [0.0239 sec]
def fun_part_1_kind_of_like_improved_or_not(data):

    def parse(line):
        pattern = r"(\w+) (\d+),(\d+) through (\d+),(\d+)"
        cmd, *coords = re.search(pattern, line).groups()
        a, b, c, d = map(int, coords)
        return cmd, slice(a, c+1), slice(b, d+1)

    instructions = [*map(parse, data.splitlines())]
    grid = np.zeros((1000, 1000), int)

    for cmd, dx, dy in instructions:
        if cmd == "toggle": grid[dx, dy] ^= 1
        else: grid[dx, dy] = ["off", "on"].index(cmd)

    return grid.sum()


#🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄🥳


@timer # [0.0467 sec]
def fun_part_2(data):

    def parse(line):
        line = line.replace("turn off ", "0,").replace("turn on ", "1,")
        line = line.replace("toggle ", "-1,").replace(" through ", ",")
        return [*map(int, line.split(","))]

    def toggle(grid, instruction, coords):
        a, b, c, d = coords
        area = grid[a:c+1, b:d+1]
        if instruction ==  0: area[:] = np.maximum(area - 1, 0)
        if instruction ==  1: area[:] += 1
        if instruction == -1: area[:] += 2

    instructions = [*map(parse, data.splitlines())]
    grid = np.zeros((1000, 1000), int)

    for instruction, a, b, c, d in instructions:
        toggle(grid, instruction, (a, b, c, d))

    return grid.sum()


@timer # [0.0482 sec]
def fun_part_2_kind_of_like_improved_or_not(data):

    def parse(line):
        pattern = r"(\w+) (\d+),(\d+) through (\d+),(\d+)"
        cmd, *coords = re.search(pattern, line).groups()
        a, b, c, d = map(int, coords)
        return cmd, slice(a, c+1), slice(b, d+1)

    instructions = [*map(parse, data.splitlines())]
    grid = np.zeros((1000, 1000), int)

    for cmd, dx, dy in instructions:
        area = grid[dx, dy]
        if cmd == "off": area[:] = np.maximum(area - 1, 0)
        else: area[:] += {"on": 1, "toggle": 2}[cmd]

    return grid.sum()


#🎄❄🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🧝
