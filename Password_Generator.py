from Functions import *


# ============================================================
# Main program
# ============================================================

def main():

    print()
    print("=" * 50)
    print("       RUBIK CUBE PASSWORD GENERATOR")
    print("=" * 50)

    print()
    print("Available moves:")
    print("F  = Front")
    print("B  = Back")
    print("U  = Top")
    print("D  = Bottom")
    print("R  = Right")
    print("L  = Left")

    print()
    print("Examples:")
    print("R U R' F2")
    print("RUR'F2")
    print("R2 U2 F B'")

    # --------------------------------------------------------
    # Shift
    # --------------------------------------------------------

    chars =input("\nEnter a secret-alphabet-list: ").replace(" ","_")
    temp = chars
    while len(temp) < 54:
        temp += chars
    chars = temp[0:54]

    while True:

        try:

            shift = int(
                input(
                    "\nEnter your shift number: "
                )
            )

            break

        except ValueError:

            print(
                "Please enter a valid number."
            )

    # --------------------------------------------------------
    # Moves
    # --------------------------------------------------------

    moves = input(
        "\nEnter your secret Rubik moves: "
    ).strip()

    # --------------------------------------------------------
    # توليد Password
    # --------------------------------------------------------

    try:

        password, cube, mapping = generate_password(
            shift,
            moves,
            chars
        )

    except ValueError as error:

        print()
        print("ERROR:")
        print(error)
        return

    # --------------------------------------------------------
    # Results
    # --------------------------------------------------------

    print()

    print("=" * 50)
    print("GENERATED PASSWORD")
    print("=" * 50)

    print(password)

    print("=" * 50)

    # --------------------------------------------------------
    # Final cube
    # --------------------------------------------------------

    print_cube(cube)

    # --------------------------------------------------------
    # if user wants to see the mapping
    # --------------------------------------------------------

    show_mapping = input(
        "\nShow character mapping? (yes/no): "
    ).strip().lower()

    if show_mapping == "yes":

        print_mapping(mapping)


# ============================================================
# runs the program
# ============================================================

if __name__ == "__main__":
    main()