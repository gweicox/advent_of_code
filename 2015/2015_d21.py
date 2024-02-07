#🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎅 Python 3.12.1 🎄


import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))
from tools import timer


with open("2015_d21.txt") as f: # 🥂
    data = f.read().strip()


#🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄⛄


from itertools import combinations as comb


shop = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3"""


@timer # [0.0006 sec]
def fun_part_1(data, shop):
    boss_stats = [int(line.split(": ")[1]) for line in data.splitlines()]
    shop = [table.splitlines()[1:] for table in shop.split("\n\n")]
    weapons = [[*map(int, row.split()[1:])] for row in shop[0]]
    armor = [[*map(int, row.split()[1:])] for row in shop[1]] + [[0, 0, 0]]
    rings = [[*map(int, row.split()[2:])] for row in shop[2]] + [[0, 0, 0], [0, 0, 0]]

    def did_player_win(player_stats, boss_stats):
        d_1 = max(1, boss_stats[1] - player_stats[2])
        d_2 = max(1, player_stats[1] - boss_stats[2])
        N_1 = player_stats[0] // d_1 + bool(player_stats[0] % d_1)
        N_2 = boss_stats[0] // d_2 + bool(boss_stats[0] % d_2)
        return N_2 <= N_1

    min_cost, hit_points = float("inf"), 100

    for (cost_r1, damage_r1, armor_r1), (cost_r2, damage_r2, armor_r2) in comb(rings, 2):
        for cost_w, damage_w, _ in weapons:
            for cost_a, _, armor_a in armor:
                curr_cost = cost_r1 + cost_r2 + cost_w + cost_a
                curr_damage = damage_r1 + damage_r2 + damage_w
                curr_armor = armor_r1 + armor_r2 + armor_a

                if did_player_win((hit_points, curr_damage, curr_armor), boss_stats):
                    min_cost = min(min_cost, curr_cost)

    return min_cost


@timer # [_ sec]
def fun_part_1_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄🥳


@timer # [0.0005 sec]
def fun_part_2(data, shop):
    boss_stats = [int(line.split(": ")[1]) for line in data.splitlines()]
    shop = [table.splitlines()[1:] for table in shop.split("\n\n")]
    weapons = [[*map(int, row.split()[1:])] for row in shop[0]]
    armor = [[*map(int, row.split()[1:])] for row in shop[1]] + [[0, 0, 0]]
    rings = [[*map(int, row.split()[2:])] for row in shop[2]] + [[0, 0, 0], [0, 0, 0]]

    def did_player_win(player_stats, boss_stats):
        d_1 = max(1, boss_stats[1] - player_stats[2])
        d_2 = max(1, player_stats[1] - boss_stats[2])
        N_1 = player_stats[0] // d_1 + bool(player_stats[0] % d_1)
        N_2 = boss_stats[0] // d_2 + bool(boss_stats[0] % d_2)
        return N_2 <= N_1

    max_cost, hit_points = 0, 100

    for (cost_r1, damage_r1, armor_r1), (cost_r2, damage_r2, armor_r2) in comb(rings, 2):
        for cost_w, damage_w, _ in weapons:
            for cost_a, _, armor_a in armor:
                curr_cost = cost_r1 + cost_r2 + cost_w + cost_a
                curr_damage = damage_r1 + damage_r2 + damage_w
                curr_armor = armor_r1 + armor_r2 + armor_a

                if not did_player_win((hit_points, curr_damage, curr_armor), boss_stats):
                    max_cost = max(max_cost, curr_cost)

    return max_cost


@timer # [_ sec]
def fun_part_2_kind_of_like_improved_or_not(data):
    pass


#🎄❄🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🧝
