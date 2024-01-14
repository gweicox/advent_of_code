#🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎅 Python 3.12.1 🎄


import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))
from tools import timer


data = "..." # your puzzle input 🥂


#🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄⛄

from string import ascii_lowercase
from itertools import groupby, pairwise


@timer # [0.3079 sec]
def fun_part_1(data):
    get_threes = lambda s: {a + b + c for a, b, c in zip(s, s[1:], s[2:])}
    abc_xyz = get_threes(ascii_lowercase)

    next_letters = {a: b for a, b in pairwise(ascii_lowercase)}
    next_letters.update({"h": "j", "k": "m", "n": "p"})

    def is_valid_password(password):
        if not (abc_xyz & get_threes(password)): return False
        group_lens = [n for _, g in groupby(password) if (n:=len([*g])) > 1]
        return len(group_lens) > 1 or bool(set(group_lens)-{2,3})

    def get_next_word(word):
        if not word: return "a"
        if word[-1] != "z": return word[:-1] + next_letters[word[-1]]
        return get_next_word(word[:-1]) + "a"

    curr_word = data

    while True:
        curr_word = get_next_word(curr_word)
        if is_valid_password(curr_word):
            return curr_word


@timer # [_ sec]
def fun_part_1_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄🥳


@timer # [1.1372 sec]
def fun_part_2(data):
    get_threes = lambda s: {a + b + c for a, b, c in zip(s, s[1:], s[2:])}
    abc_xyz = get_threes(ascii_lowercase)

    next_letters = {a: b for a, b in pairwise(ascii_lowercase)}
    next_letters.update({"h": "j", "k": "m", "n": "p"})

    def is_valid_password(password):
        if not (abc_xyz & get_threes(password)): return False
        group_lens = [n for _, g in groupby(password) if (n:=len([*g])) > 1]
        return len(group_lens) > 1 or bool(set(group_lens)-{2,3})

    def get_next_word(word):
        if not word: return "a"
        if word[-1] != "z": return word[:-1] + next_letters[word[-1]]
        return get_next_word(word[:-1]) + "a"

    curr_word, n = data, 0

    while n < 2:
        curr_word = get_next_word(curr_word)
        if is_valid_password(curr_word):
            n += 1

    return curr_word


@timer # [_ sec]
def fun_part_2_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🧝
