import math

def find_next_square(sq):
  if math.sqrt(sq) % 1 != 0:
    return -1
  else:
    nextps = sq + 1
    while math.sqrt(nextps) % 1 != 0:
      nextps += 1
    return nextps
