#🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎅 Python 3.12.1 🎄


import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))
from tools import timer


with open("2015_d18.txt") as f: # 🥂
    data = f.read().strip()


#🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄⛄


@timer # [0.8381 sec]
def fun_part_1(data, n_steps=100):
    table = [[x for x in line] for line in data.splitlines()]
    N, M = len(table), len(table[0])

    def get_light_neighbors_num(i, j, table, N, M):
        num = 0
        for di, dj in ((-1,0),(0,-1),(1,0),(0,1),(1,1),(-1,1),(-1,-1),(1,-1)):
            if 0 <= (i + di) < N and 0 <= (j + dj) < M:
                if table[i + di][j + dj] == "#":
                    num += 1
        return num

    for _ in range(n_steps):
        elfie = [["."] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                num = get_light_neighbors_num(i, j, table, N, M)
                if (num == 3) or (table[i][j] == "#" and num == 2):
                    elfie[i][j] = "#"
        table = elfie

    return sum(sum(e == "#" for e in row) for row in table)


@timer # [1.5670 sec]
def fun_part_1_kind_of_like_improved_or_not(data, n_steps=100):
    lights = {(x, y) for y, line in enumerate(data.splitlines())
                     for x, e    in enumerate(line) if e == '#'}

    neighbours = lambda x, y: sum((_x, _y) in lights for _x in (x-1, x, x+1)
                              for _y in (y-1, y, y+1) if (_x, _y) != (x, y))

    for _ in range(n_steps):
        lights = {(x, y) for x in range(100) for y in range(100)
                         if (num:= neighbours(x, y)) == 3
                         or (x, y) in lights and num == 2}

    return len(lights)


#🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🎄🥳


@timer # [0.8394 sec]
def fun_part_2(data, n_steps=100):
    table = [[x for x in line] for line in data.splitlines()]
    N, M = len(table), len(table[0])

    def get_light_neighbors_num(i, j, table, N, M):
        num = 0
        for di, dj in ((-1,0),(0,-1),(1,0),(0,1),(1,1),(-1,1),(-1,-1),(1,-1)):
            if 0 <= (i + di) < N and 0 <= (j + dj) < M:
                if table[i + di][j + dj] == "#":
                    num += 1
        return num

    for _ in range(n_steps):
        elfie = [["."] * M for _ in range(N)]
        elfie[0][0] = elfie[0][M-1] = elfie[N-1][0] = elfie[N-1][M-1] = "#"
        for i in range(N):
            for j in range(M):
                num = get_light_neighbors_num(i, j, table, N, M)
                if (num == 3) or (table[i][j] == "#" and num == 2):
                    elfie[i][j] = "#"
        table = elfie

    return sum(sum(e == "#" for e in row) for row in table)


@timer # [1.5592 sec]
def fun_part_2_kind_of_like_improved_or_not(data, n_steps=100):
    corners = {(0, 0), (0, 99), (99, 0), (99, 99)}
    lights = corners | {(x, y) for y, line in enumerate(data.splitlines())
                               for x, e    in enumerate(line) if e == '#'}

    neighbours = lambda x, y: sum((_x, _y) in lights for _x in (x-1, x, x+1)
                              for _y in (y-1, y, y+1) if (_x, _y) != (x, y))

    for _ in range(n_steps):
        lights = corners | {(x, y) for x in range(100) for y in range(100)
                                   if (num:= neighbours(x, y)) == 3
                                   or (x, y) in lights and num == 2}

    return len(lights)


#🎄❄🎄❄🎄❄🎄❄🎄🌞🎄❄🎄❄🎄❄🎄❄🎄❄🎄❄🧝
