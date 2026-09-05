import numpy as np
import random

cube = {
    'Top': np.array([
        ['W', 'W', 'W'],
        ['W', 'W', 'W'],
        ['W', 'W', 'W']
    ]),
    'Bottom': np.array([
        ['Y', 'Y', 'Y'],
        ['Y', 'Y', 'Y'],
        ['Y', 'Y', 'Y']
    ]),
    'Right': np.array([
        ['R', 'R', 'R'],
        ['R', 'R', 'R'],
        ['R', 'R', 'R']
    ]),
    'Left': np.array([
        ['O', 'O', 'O'],
        ['O', 'O', 'O'],
        ['O', 'O', 'O']
    ]),
    'Front': np.array([
        ['G', 'G', 'G'],
        ['G', 'G', 'G'],
        ['G', 'G', 'G']
    ]),
    'Back': np.array([
        ['B', 'B', 'B'],
        ['B', 'B', 'B'],
        ['B', 'B', 'B']
    ])
}

moves_name = {'F': 'Front', 'B': 'Back', 'U': 'Top', 'D': 'Bottom', 'R': 'Right', 'L': 'Left'}

map = {
    'F': [('Bottom', 'row', 0), ('Left', 'col', 2), ('Top', 'row', 2), ('Right', 'col', 0)],
    'B': [('Right', 'col', 2), ('Top', 'row', 0), ('Left', 'col', 0), ('Bottom', 'row', 2)],
    'U': [('Back', 'row', 2), ('Right', 'row', 0), ('Front', 'row', 0), ('Left', 'row', 0)],
    'D': [('Back', 'row', 0), ('Left', 'row', 2), ('Front', 'row', 2), ('Right', 'row', 2)],
    'R': [('Front', 'col', 2), ('Top', 'col', 2), ('Back', 'col', 2), ('Bottom', 'col', 2)],
    'L': [('Front', 'col', 0), ('Bottom', 'col', 0), ('Back', 'col', 0), ('Top', 'col', 0)],
}

print(cube['Top'])

def change_edges(cube: dict, move_name: str, dir: int):
    edges = map[move_name][::dir]
    temp = []

    for face, type_, index in edges:
        if type_ == 'row':
            data = cube[face][index, :].copy()
        else:
            data = cube[face][:, index].copy()
        temp.append(data)

    if move_name in ['D', 'U']:
        if dir == 1:
            temp[0], temp[-1] = temp[0][::-1], temp[-1][::-1]
        else:
            temp[-1], temp[2] = temp[-1][::-1], temp[2][::-1]
    elif (move_name == 'F') or (move_name == 'B'):
        temp[1], temp[3] = temp[1][::-1], temp[3][::-1]

    for i in range(len(edges)):
        face, type_, index = edges[i]
        old_data = temp[i - 1]

        if type_ == 'row':
            cube[face][index, :] = old_data
        else:
            cube[face][:, index] = old_data

def rotate(cube: dict, move_name: str, dir: int, times: int):
    for _ in range(times):
        cube[moves_name[move_name]] = np.rot90(cube[moves_name[move_name]], -dir)
        change_edges(cube, move_name, dir)

main = input("Should I scramble it?")
if main.strip().lower() == "yes":
    mods = ["", "'", "2"]
    all_moves = []
    pre = move = None

    for _ in range(20):
        while pre == move:
            move = random.choice(list(moves_name.keys()))
        pre = move
        x = move + random.choice(mods)
        all_moves.append(x)
        move_ = times = dir = None
        i = 0
        move_ = x[i] if x[i].isalpha() and x[i] in moves_name else None
        if move_:
            i += 1
            if i < len(x) and x[i] == "'":
                dir = -1
                i += 1
            else:
                dir = 1
            if i < len(x) and x[i].isdigit():
                times = int(x[i:])

            rotate(cube, move_name=move_, dir=dir, times=1 if not times else times)
    print(all_moves)

while True:
    for face, matrix in cube.items():
        print(f"{face} face:")
        print(matrix)
        print()
    print("-"*25)
    response = input("Enter ur next move:").strip()
    move = times = dir = None
    if response:
        i = 0
        move = response[i] if response[i].isalpha() and response[i] in moves_name else None
        if move:
            i+=1
            if i < len(response) and response[i] == "'":
                dir = -1
                i += 1
            else:
                dir = 1
            if i < len(response) and response[i].isdigit():
                times = int(response[i:])

            rotate(cube, move_name= move, dir= dir, times= 1 if not times else times)


