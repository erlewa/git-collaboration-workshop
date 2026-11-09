def is_edge(i, j, dims):
  """Determine if cell (x, y) is on the edge of the box described by dims

  Args:
    x (int): The x coordinate of the cell 
    y (int): The y coordinate of the cell
    dims ((int, int)): The dimensions of the box

  Returns:
    bool: True if cell (x, y) is on the edge of the box, otherwise false
  """
  if i == 0 or j == 0:
    return True
  
  if i == dims[0]-1 or j == dims[1]-1:
    return True

  return False


def print_box(width, height, border = "*", fill = " "):
  """Print the outline of a box

  Args:
    width  (int): The width of the box
    height (int): The height of the box
    border (str): Single character used for the border of the box
    fill   (str): Single character used for the interior of the box
  """

  out = ""
  for y in range(height):
    for x in range(width):
      if is_edge(x, y, (width, height)):
        out += border
      else:
        out += fill 

    out += "\n" 

  print(out, end="")


def main():
  while True:
    try:
      width = int(input("Enter box width (0 to exit): "))
      if width == 0:
        break
      height = int(input("Enter box height (0 to exit): "))
      if height == 0:
        break
      border = input("Enter character to use for the border of the box (0 to exit): ")
      if border == "0":
        break
      fill = input("Enter character to use for the interior of the box (0 to exit): ")
      if fill == "0":
        break

    except ValueError:
      print("Please enter a positive integer")
      continue

    print_box(width, height, border=border, fill=fill)

if __name__ == "__main__":
  main()
