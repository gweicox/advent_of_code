#🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎅 Python 3.12.1 🎄


import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))
from tools import timer


with open("2015_d16.txt") as f: # 🥂
    data = f.read().strip()

    message = """children: 3
            cats: 7
            samoyeds: 2
            pomeranians: 3
            akitas: 0
            vizslas: 0
            goldfish: 5
            trees: 3
            cars: 2
            perfumes: 1"""


#🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄⛄


@timer # [0.0073 sec]
def fun_part_1(data, message):
    message = message.replace("\n",",").replace(":","=")
    message = eval(f"dict({message})")

    sues = [line.split(": ", 1)[1] for line in data.splitlines()]
    sues = [eval(f'dict({line.replace(":","=")})') for line in sues]

    for indx, dct in enumerate(sues, 1):
        ans = True
        for k, v in dct.items():
            if k not in message:
                ans = False
                break
            if v != message[k]:
                ans = False
                break  
        if ans:
            return indx


@timer # [0.0015 sec]
def fun_part_1_kind_of_like_improved_or_not(data, message):
    create_items_set = lambda str_: set(eval(f"dict({str_})").items())
    message = create_items_set(message.replace("\n",",").replace(":","="))

    sues = (line.split(": ", 1)[1] for line in data.splitlines())
    sues = (create_items_set(line.replace(":","=")) for line in sues)

    return next(indx for indx, items_set in enumerate(sues, 1) if items_set <= message)


#🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄🥳


@timer # [0.0067 sec]
def fun_part_2(data, message):
    message = message.replace("\n",",").replace(":","=")
    message = eval(f"dict({message})")

    sues = [line.split(": ", 1)[1] for line in data.splitlines()]
    sues = [eval(f'dict({line.replace(":","=")})') for line in sues]

    for indx, dct in enumerate(sues, 1):
        ans = True
        for k, v in dct.items():
            if k not in message:
                ans = False
                break
            if k in ("cats", "trees"):
                if v <= message[k]:
                    ans = False
                    break
            elif k in ("pomeranians", "goldfish"):
                if v >= message[k]:
                    ans = False
                    break
            else:
                if v != message[k]:
                    ans = False
                    break  
        if ans:
            return indx


@timer # [0.0061 sec]
def fun_part_2_kind_of_like_improved_or_not(data, message):
    create_items_dct = lambda str_: eval(f"dict({str_})")
    message = create_items_dct(message.replace("\n",",").replace(":","="))

    sues = (line.split(": ", 1)[1] for line in data.splitlines())
    sues = (create_items_dct(line.replace(":","=")) for line in sues)

    def is_match(items_dct):
        def f(item, val):
            if item in ("cats", "trees"): return val > message[item]
            if item in ("pomeranians", "goldfish"): return val < message[item]
            return val == message[item]
        return all(f(item, val) for item, val in items_dct.items())

    return next(indx for indx, items_dct in enumerate(sues, 1) if is_match(items_dct))


#🎄❄🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🧝
