def is_edge(i, j, dims):
  if i == 0 or j == 0:
    return True
  
  if i == dims[0]-1 or j == dims[1]-1:
    return True
  print("i: ", i, "  j: ", j, "  dims: ", dims) 
  return False

def print_box(width, height):
  for i in height:
    for j in width:
      c = " "
      if is_edge(i,j):
        c = "*"
  print(
        "**********\n"
        "*        *\n"
        "**********"
       )


