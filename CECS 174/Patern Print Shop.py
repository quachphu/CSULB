# In A
def print_solid_rectangle(symbol, rows, columns):
    for i in range(rows):
        for j in range(columns):
            print(symbol, end=" ")
        print()


def print_hollow_rectangle(symbol, rows, columns):
    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                print(symbol, end=" ")
            else:
                print(" ", end=" ")
        print()

# In B

def print_half_pyramid(rows, symbol):
    if symbol.isdigit():
        for i in range(1, rows + 1):
            for j in range(1, i + 1):
                print(j, end=' ')
            print()
    else:
        for i in range(1, rows + 1):
            print(symbol * i)


def print_inverted_half_pyramid(rows, symbol):
    if symbol.isdigit():
        for i in range(rows, 0, -1):
            for j in range(1, i + 1):
                print(j, end=' ')
            print()
    else:
        for i in range(rows, 0, -1):
            print(symbol * i)


def print_hollow_inverted_half_pyramid(rows, symbol):
    if symbol.isdigit():
        for i in range(rows, 0, -1):
            for j in range(1, i + 1):
                if j == 1 or j == i or i == rows:
                    print(j, end=' ')
                else:
                    print(" ", end=' ')
            print()
    else:
        for i in range(rows, 0, -1):
            if i == rows or i == 1:
                print(symbol * i)
            else:
                print(symbol + " " * (2 * i - 3) + symbol)

def print_hollow_half_pyramid(rows, symbol):
    if symbol.isdigit():
        for i in range(1, rows + 1):
            for j in range(1, i + 1):
                if j == 1 or j == i or i == rows:
                    print(j, end=' ')
                else:
                    print(" ", end=' ')
            print()
    else:
        for i in range(1, rows + 1):
            if i == 1 or i == rows:
                print(symbol * i)
            else:
                print(symbol + " " * (i - 2) + symbol)

def print_full_pyramid(rows, symbol):
    if symbol.isdigit():
        for i in range(1, rows + 1):
            print(" " * (rows - i), end="")
            for j in range(1, i + 1):
                print(j, end=' ')
            print()
    else:
        for i in range(1, rows + 1):
            print(" " * (rows - i) + symbol * (2 * i - 1))


def print_inverted_full_pyramid(rows, symbol):
    if symbol.isdigit():
        for i in range(rows, 0, -1):
            print(" " * (rows - i), end="")
            for j in range(1, i + 1):
                print(j, end=' ')
            print()
    else:
        for i in range(rows, 0, -1):
            print(" " * (rows - i) + symbol * (2 * i - 1))


def print_hollow_inverted_full_pyramid(rows, symbol):
    if symbol.isdigit():
        for i in range(rows, 0, -1):
            print(" " * (rows - i), end="")
            for j in range(1, i + 1):
                if j == 1 or j == i or i == rows:
                    print(j, end=' ')
                else:
                    print(" ", end=' ')
            print()
    else:
        for i in range(rows, 0, -1):
            if i == rows or i == 1:
                print(" " * (rows - i) + symbol * (2 * i - 1))
            else:
                print(" " * (rows - i) + symbol + " " * (2 * i - 3) + symbol)


def print_hollow_inverted_half_pyramid(rows, symbol):
    if symbol.isdigit():
        for i in range(rows, 0, -1):
            for j in range(1, i + 1):
                if j == 1 or j == i or i == rows:
                    print(j, end=' ')
                else:
                    print(" ", end=' ')
            print()
    else:
        for i in range(rows, 0, -1):
            if i == rows or i == 1:
                print(symbol * i)
            else:
                print(symbol + " " * (i - 2) + symbol)
                
# In C
def print_solid_diamond(rows, symbol):
    for i in range(rows - 1):
        for j in range(i, rows):
            print(" ", end="")
        for j in range(i):
            print(symbol, end="")
        for j in range(i + 1):
            print(symbol, end="")
        print()

    for i in range(rows):
        for j in range(i + 1):
            print(" ", end="")
        for j in range(i, rows - 1):
            print(symbol, end="")
        for j in range(i, rows):
            print(symbol, end="")
        print()


def print_hollow_diamond(rows, symbol):
    for i in range(rows - 1):
        for j in range(i, rows - 1):
            print(" ", end="")
        for j in range(i):
            if j == 0:
                print(symbol, end='')
            else:
                print(" ", end="")
        for j in range(i + 1):
            if j == i:
                print(symbol, end='')
            else:
                print(" ", end="")
        print()

    for i in range(rows):
        for j in range(i):
            print(" ", end="")
        for j in range(i, rows):
            if j == i:
                print(symbol, end='')
            else:
                print(" ", end="")
        for j in range(i, rows - 1):
            if j == rows - 2:
                print(symbol, end='')
            else:
                print(" ", end="")
        print()


def print_solid_half_diamond(rows, symbol):
    for i in range(rows - 1):
        for j in range(i, rows):
            print('', end='')
        for j in range(i):
            print(symbol, end='')
        for j in range(i + 1):
            print(symbol, end='')
        print()

    for i in range(rows):
        for j in range(i + 1):
            print("", end='')
        for j in range(i, rows - 1):
            print(symbol, end='')
        for j in range(i, rows):
            print(symbol, end='')
        print()


def main():
    while True:
        print("Welcome to Pattern Print Shop. Please select from the following menu:")
        print("A- To print a rectangle")
        print("B- To print Pyramid pattern")
        print("C- To print Diamond Pattern")
        print("Q- To quit.")

        choice = input("Enter your choice: ")

        if choice == 'A':
            while True:
                while True:
                    rows = int(
                        input("Enter the number of rows for the rectangle: "))
                    if rows > 0:
                        break
                while True:
                    columns = int(
                        input("Enter the number of columns for the rectangle: "))
                    if columns > 0:
                        break

                symbol = input("Enter the symbol you want to use: ")
                print("1- Hollow Rectangle")
                print("2- Solid Rectangle")
                print("0- Return to main menu ")
                rectangle_type = int(input("Enter your choice (0/1/2): "))

                if rectangle_type == 1:
                    print("Hollow Rectangle")
                    print_hollow_rectangle(symbol, rows, columns)
                elif rectangle_type == 2:
                    print("Solid Rectangle")
                    print_solid_rectangle(symbol, rows, columns)
                elif rectangle_type == 0:
                    break
                else:
                    print("Invalid choice.")
        elif choice == 'B':
            while True:
                while True:
                    rows = int(input("Enter the height of the pyramid: "))
                    if rows > 0:
                        break
                symbol = input(
                    "Enter the symbol you want to use(!, @, #, $, %, ^, &, *): ")
                print("Pyramid Pattern Menu:")
                print("1- Half Pyramid")
                print("2- Full Pyramid")
                print("0- Return to main menu ")
                pyramid_type = int(input("Enter your choice (0/1/2): "))
                if pyramid_type == 1:
                    while True:
                        print("Half Pyramid Pattern Menu: ")
                        print("1- Half Pyramid")
                        print("2- Inverted Half Pyramid")
                        print("3- Hollow Inverted Half Pyramid")
                        print("4- Hollow Half Pyramid")
                        print("0- Return to main menu ")
                        half_pyramid_type = int(
                            input("Enter your choice (0/1/2/3): "))
                        if half_pyramid_type == 1:
                            print("Half Pyramid")
                            print_half_pyramid(rows, symbol)
                        elif half_pyramid_type == 2:
                            print("Inverted Half Pyramid")
                            print_inverted_half_pyramid(rows, symbol)
                        elif half_pyramid_type == 3:
                            print("Hollow Inverted Half Pyramid")
                            print_hollow_inverted_half_pyramid(rows, symbol)
                        elif half_pyramid_type==4: 
                            print("Hollow Half Pyramid")
                            print_hollow_half_pyramid(rows, symbol)
                        elif half_pyramid_type == 0:
                            break
                        else:
                            print("Invalid choice.")
                elif pyramid_type == 2:
                    while True:
                        print("Full Pyramid Pattern Menu ")
                        print("1- Full Pyramid")
                        print("2- Inverted Full Pyramid")
                        print("3- Hollow Inverted Full Pyramid")
                        print("4- Hollow Inverted Half Pyramid")
                        print("0- Return to main menu ")
                        full_pyramid_type = int(
                            input("Enter your choice (0/1/2/3): "))
                        if full_pyramid_type == 1:
                            print("Full Pyramid")
                            print_full_pyramid(rows, symbol)
                        elif full_pyramid_type == 2:
                            print("Inverted Full Pyramid")
                            print_inverted_full_pyramid(rows, symbol)
                        elif full_pyramid_type == 3:
                            print("Hollow Inverted Full Pyramid")
                            print_hollow_inverted_full_pyramid(rows, symbol)
                        elif full_pyramid_type ==4:
                            print("Hollow Inverted Half Pyramid")
                            print_hollow_inverted_half_pyramid(rows, symbol)
                        elif full_pyramid_type == 0:
                            break
                        else:
                            print("Invalid choice.")
                elif pyramid_type == 0:
                    break
                else:
                    print("Invalid choice.")

        elif choice == 'C':
            while True:
                print("Diamond Pattern Menu:")
                rows = int(input("Enter the number of rows for the diamond: "))
                symbol = input("Enter the symbol you want to use: ")
                print("1- Solid Diamond")
                print("2- Hollow Diamond")
                print("3- Solid Half Diamond")
                print("0- Return to main menu")
                diamond_type = int(input("Enter your choice (0/1/2/3): "))
                if diamond_type == 1:
                    print("Solid Diamond")
                    print_solid_diamond(rows, symbol)
                elif diamond_type == 2:
                    print("Hollow Diamond")
                    print_hollow_diamond(rows, symbol)
                elif diamond_type == 3:
                    print("Solid Half Diamond")
                    print_solid_half_diamond(rows, symbol)
                elif diamond_type == 0:
                    break
                else:
                    print("Invalid choice.")

        elif choice == 'Q':
            print("Thank you for your business!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
