#             1
#          3     5
#       7     9    11
#   13    15    17    19
#21    23    25    27    29
#...

def row_sum_odd_numbers(n):
  middle_l = 0
  middle_2 = 0
  the_sum = 0
  total = 0
  middle = n ** 2
  if middle % 2 == 0:
    middle_l = middle - 1
    the_sum += middle_l
    middle_r = middle + 1
    the_sum += middle_r
    total += 2
  else:
    the_sum += middle
    total += 1
  while total < n:
    if middle_l > 0 and middle_r > 0:
      the_sum += middle_l - 2
      the_sum += middle_r + 2
      total += 2
    else:
      the_sum += middle - 2 
      the_sum += middle + 2
      total += 2
  return the_sum
  
