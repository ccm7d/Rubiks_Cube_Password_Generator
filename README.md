# Rubik's Cube Password Generator

A Python project that generates passwords using **Rubik's Cube movements** and a customizable character list.


> **Note:** This project is for experimentation and learning. It is not necessarily recommended for protecting your real-world accounts.

## 💡 How Does It Work?

The project combines a **Rubik's Cube**, a customizable character list, and user-defined cube movements to generate a password.

The basic process is:

```text
Character List
      ↓
Character Shift
      ↓
Map Characters to the 54 Cube Stickers
      ↓
Apply User's Rubik's Cube Movements
      ↓
Read the Cube Using a Fixed Pattern
      ↓
Generate Password
```

---

## 1. Secret Alphabet List

The program uses a customizable list of characters called:

```text
secret-alphabet-list
```

The list can contain:

* Uppercase letters
* Lowercase letters
* Numbers
* Symbols

For example:

```text
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
0123456789
!@#$%^&*()
```

The character list can also be customized depending on the password requirements.

For example, if numbers are not required, the list can contain only letters:

```text
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
```

The same idea can be applied to symbols.

---

## 2. Character Shift

The user chooses a number called `shift`.

The shift changes the order of the characters in the `secret-alphabet-list`.

For example, with:

```text
ABCDEF
```

a shift of `2` produces:

```text
CDEFAB
```

A shift of `0` keeps the original order.

This concept is inspired by the idea of the **Caesar Cipher**, where characters are shifted by a specific amount.

---

## 3. Mapping Characters to the Rubik's Cube

A standard 3×3 Rubik's Cube contains **54 stickers**:

```text
6 faces × 9 stickers = 54 stickers
```

The program initially represents the stickers using names such as:

```text
W1 W2 W3
W4 W5 W6
W7 W8 W9
```

and:

```text
Y1 Y2 Y3
Y4 Y5 Y6
Y7 Y8 Y9
```

along with the other four faces:

```text
R1-R9
O1-O9
G1-G9
B1-B9
```

After applying the selected character shift, each of the 54 sticker positions is mapped to a character from the `secret-alphabet-list`.

For example:

```text
W1 → A
W2 → B
W3 → C
...
```

The mapping is created in this face order:

```text
Top
Bottom
Right
Left
Front
Back
```

---

## 4. User's Rubik's Cube Movements

The user enters a sequence of Rubik's Cube movements.

For example:

```text
R U R'
```

Spaces are automatically removed, so the same input can be written as:

```text
RUR'
```

The program supports the standard face movements:

```text
F
B
U
D
R
L
```

It also supports reverse movements using `'`.

For example:

```text
R'
U'
F'
```

Multiple rotations can also be specified using a number:

```text
R2
U2
F2
```

The program applies these movements to the virtual Rubik's Cube.

---

## 5. Password Pattern

After all movements are applied, the program reads the cube using a predefined pattern.

The current pattern reads the faces in this order:

```text
Top
Bottom
Right
Left
Front
Back
```

Each face is then read from left to right and top to bottom.

For example:

```text
1 2 3
4 5 6
7 8 9
```

The 54 resulting characters are combined into one string.

---

## 🔐 Password Generation

The final password is generated from the characters found on the cube after applying the user's movements.

Conceptually:

```text
Secret Alphabet
      +
Shift
      +
Rubik's Cube Movements
      +
Reading Pattern
      ↓
Generated Password
```

The current implementation generates a **54-character password**, corresponding to all 54 stickers of the Rubik's Cube.

---

## 🎯 Example

Before applying any movements, the cube contains sticker identifiers:

```text
W1 W2 W3
W4 W5 W6
W7 W8 W9
```

After mapping the stickers to characters, the same positions may represent:

```text
A B C
D E F
G H I
```

After applying the user's Rubik's Cube movements, the positions change.



|   |   |   |
| - | - | - |
| 🟦 | 🟦 | 🟥 |
| 🟩 | ⬜ | 🟩 |
| 🟧 | 🟥 | 🟥 |

Becomes:

|   |   |   |
| - |---| - |
| A | 7 | K |
| P | E | 2 |
| M | Q | 9 |



The program then reads the cube according to the predefined pattern and converts the resulting sticker identifiers into the corresponding characters.

The result is the generated password.

---

## 📁 Files

* `Password_Generator.py` - Main program for generating passwords.
* `Functions.py` - Contains the Rubik's Cube logic, character mapping, movement handling, and password generation.
* `Rubiks_Cube.py` - Interactive Rubik's Cube simulator.

## ⚙️ Requirements

* Python 3.x
* NumPy

## 📦 Installation

```bash
pip install -r requirements.txt
```

## ▶️ Run

```bash
python Password_Generator.py
```
