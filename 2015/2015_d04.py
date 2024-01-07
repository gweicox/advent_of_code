#🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎅 Python 3.12.1 🎄


import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))
from tools import timer


data = "..." # your secret key


#🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄⛄

from hashlib import md5
from itertools import count


@timer # [0.2223 sec]
def fun_part_1(data):
    num = 1
    while True:
        if md5((data + str(num)).encode('utf-8')).hexdigest()[:5] == "00000":
            return num
        num += 1


@timer # [0.2200 sec]
def fun_part_1_kind_of_like_improved_or_not(data):
    return next(x for x in count() if md5((data + str(x)).encode('utf-8')).hexdigest().startswith("00000"))


#🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄🥳


@timer # [6.4850 sec]
def fun_part_2(data):
    num = 1
    while True:
        if md5((data + str(num)).encode('utf-8')).hexdigest()[:6] == "000000":
            return num
        num += 1


@timer # [6.9154 sec]
def fun_part_2_kind_of_like_improved_or_not(data):
    return next(x for x in count() if md5((data + str(x)).encode('utf-8')).hexdigest().startswith("000000"))


#🎄❄🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🧝
