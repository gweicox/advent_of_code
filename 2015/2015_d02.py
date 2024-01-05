#🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎅 Python 3.12.1 🎄


with open("2015_d02.txt") as f:
    data = f.read().strip()


#🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄⛄

from itertools import starmap


def fun_part_1(data):
    lines = (line.split("x") for line in data.splitlines())
    lines = (sorted(map(int, line)) for line in lines)
    f = lambda L, W, H: 2 * (L * W + W * H + H * L) + L * W
    return sum(starmap(f, lines))


def fun_part_1_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄🥳


def fun_part_2(data):
    lines = (line.split("x") for line in data.splitlines())
    lines = (sorted(map(int, line)) for line in lines)
    f = lambda L, W, H: 2 * (L + W) + W * H * L
    return sum(starmap(f, lines))


def fun_part_2_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🧝

print(f"Part 1: {fun_part_1(data)}") # 3 ms ☃️
print(f"Part 2: {fun_part_2(data)}") # 3 ms 🥂
