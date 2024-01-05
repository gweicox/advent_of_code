#🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄🎅

with open("2015_d01.txt") as f:
    data = f.read().strip()

#🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄⛄


def fun_part_1(data):
    return sum((-1, 1)[symbol == "("] for symbol in data)


def fun_part_1_kind_of_like_improved_or_not(data):
    return data.count("(") - data.count(")")


#🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄🥳


def fun_part_2(data):
    curr_floor = 0
    for indx, symbol in enumerate(data, 1):
        curr_floor += (-1, 1)[symbol == "("]
        if curr_floor == -1:
            return(indx)


def fun_part_2_kind_of_like_improved_or_not(data):
    from itertools import accumulate as acc
    return [*acc((-1, 1)[x=="("] for x in data)].index(-1) + 1


#🎄❄🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄🧝

print(f"Part 1: {fun_part_1(data)}") # 4 ms ☃️
print(f"Part 2: {fun_part_2(data)}") # 2 ms 🥂
# Python 3.12.1
