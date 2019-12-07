# multiples of array index

def mult_of_index(l):
  new_list = []
  for idx, i in l:
    if i / idx % 0:
      new_list.append(i)
  return new_list
