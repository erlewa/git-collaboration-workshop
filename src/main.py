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


def print_box(width, height):
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

