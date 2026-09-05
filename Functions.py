import numpy as np
import string


# ============================================================
# Creates a new cube
# ============================================================


def create_cube():
    return {
        'Top': np.array([
            ['W1', 'W2', 'W3'],
            ['W4', 'W5', 'W6'],
            ['W7', 'W8', 'W9']
        ]),

        'Bottom': np.array([
            ['Y1', 'Y2', 'Y3'],
            ['Y4', 'Y5', 'Y6'],
            ['Y7', 'Y8', 'Y9']
        ]),

        'Right': np.array([
            ['R1', 'R2', 'R3'],
            ['R4', 'R5', 'R6'],
            ['R7', 'R8', 'R9']
        ]),

        'Left': np.array([
            ['O1', 'O2', 'O3'],
            ['O4', 'O5', 'O6'],
            ['O7', 'O8', 'O9']
        ]),

        'Front': np.array([
            ['G1', 'G2', 'G3'],
            ['G4', 'G5', 'G6'],
            ['G7', 'G8', 'G9']
        ]),

        'Back': np.array([
            ['B1', 'B2', 'B3'],
            ['B4', 'B5', 'B6'],
            ['B7', 'B8', 'B9']
        ])
    }


# ============================================================
# Movement names
# ============================================================

moves_name = {
    'F': 'Front',
    'B': 'Back',
    'U': 'Top',
    'D': 'Bottom',
    'R': 'Right',
    'L': 'Left'
}

# ============================================================
# Selecting edges for each moves
# ============================================================

edge_map = {
    'F': [
        ('Bottom', 'row', 0),
        ('Left', 'col', 2),
        ('Top', 'row', 2),
        ('Right', 'col', 0)
    ],

    'B': [
        ('Right', 'col', 2),
        ('Top', 'row', 0),
        ('Left', 'col', 0),
        ('Bottom', 'row', 2)
    ],

    'U': [
        ('Back', 'row', 2),
        ('Right', 'row', 0),
        ('Front', 'row', 0),
        ('Left', 'row', 0)
    ],

    'D': [
        ('Back', 'row', 0),
        ('Left', 'row', 2),
        ('Front', 'row', 2),
        ('Right', 'row', 2)
    ],

    'R': [
        ('Front', 'col', 2),
        ('Top', 'col', 2),
        ('Back', 'col', 2),
        ('Bottom', 'col', 2)
    ],

    'L': [
        ('Front', 'col', 0),
        ('Bottom', 'col', 0),
        ('Back', 'col', 0),
        ('Top', 'col', 0)
    ]
}


# ============================================================
# Changing edges
# ============================================================

def change_edges(cube, move_name, direction):
    edges = edge_map[move_name][::direction]

    temp = []

    for face, type_, index in edges:

        if type_ == 'row':
            data = cube[face][index, :].copy()

        else:
            data = cube[face][:, index].copy()

        temp.append(data)

    if move_name in ['D', 'U']:

        if direction == 1:
            temp[0] = temp[0][::-1]
            temp[-1] = temp[-1][::-1]

        else:
            temp[-1] = temp[-1][::-1]
            temp[2] = temp[2][::-1]

    elif move_name in ['F', 'B']:

        temp[1] = temp[1][::-1]
        temp[3] = temp[3][::-1]

    for i in range(len(edges)):

        face, type_, index = edges[i]

        old_data = temp[i - 1]

        if type_ == 'row':
            cube[face][index, :] = old_data

        else:
            cube[face][:, index] = old_data


# ============================================================
# Moving ( Rotating )
# ============================================================

def rotate(cube, move_name, direction, times):
    for _ in range(times):
        cube[moves_name[move_name]] = np.rot90(
            cube[moves_name[move_name]],
            -direction
        )

        change_edges(
            cube,
            move_name,
            direction
        )

# ============================================================
# Creates mapping & shifts it
# ============================================================

def create_mapping(shift, chars):
    shift %= len(chars)

    # shifting
    chars = chars[shift:] + chars[:shift]

    mapping = {}

    prefixes = [
        'W',  # Top
        'Y',  # Bottom
        'R',  # Right
        'O',  # Left
        'G',  # Front
        'B'  # Back
    ]

    index = 0

    for prefix in prefixes:

        for number in range(1, 10):
            mapping[f"{prefix}{number}"] = chars[index]

            index += 1

    return mapping


# ============================================================
# Reads user's movement
# ============================================================

def apply_moves(cube, moves):
    moves = moves.replace(" ", "")

    if not moves:
        raise ValueError(
            "لم تدخل أي حركات."
        )

    i = 0

    while i < len(moves):
        move = moves[i].upper()

        if move not in moves_name:
            raise ValueError(
                f"حركة غير صحيحة عند الحرف: {moves[i]}"
            )

        i += 1

        # dir
        if i < len(moves) and moves[i] == "'":

            dir = -1
            i += 1

        else:

            dir = 1

        # num of times
        if i < len(moves) and moves[i].isdigit():

            start = i

            while i < len(moves) and moves[i].isdigit():
                i += 1

            times = int(moves[start:i])

        else:

            times = 1

        if times <= 0:
            raise ValueError(
                "عدد مرات الحركة يجب أن يكون أكبر من صفر."
            )

        rotate(
            cube,
            move_name=move,
            direction=dir,
            times=times
        )


# ============================================================
# Password Pattern
# ============================================================

def create_password_pattern():
    # You can change the faces order
    faces_order = [
        'Top',
        'Bottom',
        'Right',
        'Left',
        'Front',
        'Back'
    ]

    pattern = []

    for face in faces_order:

        # You can change the order of cubes
        positions = [
            (0, 0), (0, 1), (0, 2),
            (1, 0), (1, 1), (1, 2),
            (2, 0), (2, 1), (2, 2)
        ]

        for row, col in positions:
            pattern.append((face, row, col))

    return pattern


# ============================================================
# From cube to a real password
# ============================================================

def cube_to_password(cube, mapping):
    password = []
    PASSWORD_PATTERN = create_password_pattern()

    for face, row, col in PASSWORD_PATTERN:
        # E.G:
        # W1
        # G5
        # R9
        temp = cube[face][row, col]

        character = mapping[temp]

        password.append(character)

    return ''.join(password)


# ============================================================
# Shows the cube
# ============================================================

def print_cube(cube):
    print()
    print("=" * 40)

    for face, matrix in cube.items():

        print(f"\n{face} face:")

        for row in matrix:
            print(" ".join(row))

    print("=" * 40)


# ============================================================
# Shows mapping
# ============================================================

def print_mapping(mapping):
    print()
    print("=" * 40)
    print("CHARACTER MAPPING")
    print("=" * 40)

    for sticker, character in mapping.items():
        print(
            f"{sticker:>3} -> {character}"
        )

    print("=" * 40)


# ============================================================
# Generates our password
# ============================================================

def generate_password(shift, moves, chars):
    cube = create_cube()
    mapping = create_mapping(shift, chars)

    apply_moves(
        cube,
        moves
    )

    password = cube_to_password(
        cube,
        mapping
    )

    return password, cube, mapping