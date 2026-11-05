def is_edge(i, j, dims):
  if i == 0 or j == 0:
    return True
  
  if i == dims[0]-1 or j == dims[1]-1:
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


print_box(2, 2)
