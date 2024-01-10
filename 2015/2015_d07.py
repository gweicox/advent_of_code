#🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎅 Python 3.12.1 🎄


import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))
from tools import timer


with open("2015_d07.txt") as f: # 🥂
    data = f.read().strip()


#🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄⛄


@timer # [0.0037 sec]
def fun_part_1(data):
    table = [line.split(" -> ") for line in data.splitlines()]
    G = {dest: op.split() for op, dest in table}
    ops = {"AND":"&","OR":"|","LSHIFT":"<<","RSHIFT":">>","NOT":"~","":""}
    memo = {"":""}

    def get_signal(dest):
        if dest in memo: return memo[dest]
        if dest.isdigit(): return dest
        src = ["",""] + G[dest]
        memo[dest] = eval(f"{get_signal(src[-3])}"
                          f"{ops[src[-2]]}"
                          f"{get_signal(src[-1])}")
        return memo[dest]

    return get_signal("a")


@timer # [_ sec]
def fun_part_1_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄🥳


@timer # [0.0052 sec]
def fun_part_2(data):
    table = [line.split(" -> ") for line in data.splitlines()]
    G = {dest: op.split() for op, dest in table}
    ops = {"AND":"&","OR":"|","LSHIFT":"<<","RSHIFT":">>","NOT":"~","":""}
    memo = {"":""}

    def get_signal(dest):
        if dest in memo: return memo[dest]
        if dest.isdigit(): return dest
        src = ["",""] + G[dest]
        memo[dest] = eval(f"{get_signal(src[-3])}"
                          f"{ops[src[-2]]}"
                          f"{get_signal(src[-1])}")
        return memo[dest]

    G['b'] = [str(get_signal("a"))]
    memo = {"":""}

    return get_signal("a")


@timer # [_ sec]
def fun_part_2_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🧝
