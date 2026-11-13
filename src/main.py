# A program to print boxes to the command line


def is_point_on_box_edge(x, y, dims):
    """Determine if cell (x, y) is on the edge of the box described by dims

    Args:
      x (int): The x coordinate of the cell
      y (int): The y coordinate of the cell
      dims ((int, int)): The (width, height) of the box

    Returns:
      bool: True if cell (x, y) is on the edge of the box, otherwise false
    """
    if x == 0 or y == 0:
        return True

    if x == dims[0] - 1 or y == dims[1] - 1:
        return True

    return False


def display_box_with_dimensions(width, height):
    """Print the outline of a box

    Args:
      width (int): The width of the box
      height (int): The height of the box
    """
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

        # Call print_box function with dimensions