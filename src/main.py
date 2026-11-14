# A program to print boxes to the command line


def is_edge(x, y, dims):
    if x == 0 or y == 0:
        return True

    if x == dims[0] - 1 or y == dims[1] - 1:
        return True

    return False


def print_box(width, height):
    out = ""
    for y in range(height):
        for x in range(width):
            if is_edge(x, y, (width, height)):
                out += "*"
            else:
                out += " "

        out += "\n"

    print(out, end="")


def main():
    while True:
        try:
            width = int(input("Enter the width of the box (0 to exit):"))
            if width == 0:
                break
            height = int(input("Enter the height of the box (0 to exit):"))
            if height == 0:
                break

        except ValueError:
            print("Please enter an integer value")

        print_box(width, height)


if __name__ == "__main__":
    main()