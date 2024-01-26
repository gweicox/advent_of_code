#🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎅 Python 3.12.1 🎄


import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))
from tools import timer


with open("2015_d19.txt") as f: # 🥂
    data = f.read().strip()


#🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄⛄

from collections import defaultdict


@timer # [0.0018 sec]
def fun_part_1(data):
    replacements, curr_molecule = data.split("\n\n")
    reps, molecules = defaultdict(list), set()

    for r in replacements.splitlines():
        k, v = r.split(" => ")
        reps[k].append(v)

    def get_new_molecules(mol, reps, indx, n):
        values = reps[mol[indx:indx+n]]
        return set(mol[:indx] + v + mol[indx+n:] for v in values)

    for indx in range(len(curr_molecule)):
        molecules |= get_new_molecules(curr_molecule, reps, indx, 1)
        molecules |= get_new_molecules(curr_molecule, reps, indx, 2)

    return len(molecules)


@timer # [0.0029 sec]
def fun_part_1_kind_of_like_improved_or_not(data):
    reps, molecule = data.split("\n\n")
    replacements = (r.split(" => ") for r in reps.splitlines())
    S, N = set(), len(molecule)

    for k, v in replacements:
        for indx in range(N):
            if molecule[indx:indx+len(k)] == k:
                S.add(molecule[:indx] + v + molecule[indx+len(k):])

    return len(S)


#🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄🥳


@timer # [0.0012 sec]
def fun_part_2(data):
    reps, curr_molecule = data.split("\n\n")
    replacements = (r.split(" => ")[::-1] for r in reps.splitlines())
    replacements = sorted(replacements, key=lambda x:-len(x[0]))
    steps = 0

    while curr_molecule != "e":
        steps += 1
        for k, v in replacements:
            if k in curr_molecule:
                curr_molecule = curr_molecule.replace(k, v, 1)
                break

    return steps


@timer # [_ sec]
def fun_part_2_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🧝
