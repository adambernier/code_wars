import collections as co
import itertools as it

def divide_chunks(l,n):
  for i in range(0,len(l),n):
    yield l[i:i+n]

def valid_series(row):
  dd = co.defaultdict(int)
  for num in row:
    dd[num] += 1
  vals = [v for v in dd.values()]
  if (max(vals) == 1 and
      min(vals) == 1 and
      len(vals) == len(row)):
    return True
  else:
    return False

def valid_square(square):
  vals = [v for v in square.values()]
  if (max(vals) == 1 and
      min(vals) == 1 and
      len(vals) == len(square)):
    return True
  else:
    return False
    
def valid_section(section):
  left_sq = co.defaultdict(int) 
  mid_sq = co.defaultdict(int) 
  right_sq = co.defaultdict(int)
  for row in section:
    for idx,three in enumerate(row):
      if idx == 0:
        for num in three:
          left_sq[num] += 1
      elif idx == 1:
        for num in three:
          mid_sq[num] += 1
      else:
        for num in three:
          right_sq[num] += 1
  return left_sq, mid_sq, right_sq 

def validSolution(board):
  rows = []
  cols = []
  
  # square check 
  top = []; mid = []; bot = []
  for idx,series in enumerate(board):
    if idx <= 2:
      top.append(list(divide_chunks(series,3)))
    elif idx > 2 and idx < 6:
      mid.append(list(divide_chunks(series,3)))
    else:
      bot.append(list(divide_chunks(series,3)))
  
  squares = []
  
  left_sq, mid_sq, right_sq = valid_section(top)
  
  squares.append(valid_square(left_sq))
  squares.append(valid_square(mid_sq))
  squares.append(valid_square(right_sq))
  
  left_sq, mid_sq, right_sq = valid_section(mid)
  
  squares.append(valid_square(left_sq))
  squares.append(valid_square(mid_sq))
  squares.append(valid_square(right_sq))
  
  left_sq, mid_sq, right_sq = valid_section(bot)
  
  squares.append(valid_square(left_sq))
  squares.append(valid_square(mid_sq))
  squares.append(valid_square(right_sq))
  
  if not all(sq for sq in squares):
    return False
  else:
    return True
  
  # row check
  for row in board:
    print(row)
    rows.append(valid_series(row))
  
  if not all(r for r in rows):
    return False
  
  # transpose
  board = [*zip(*board)]
  
  # column check
  for col in board:
    cols.append(valid_series(col))
  
  if not all(c for c in cols):
    return False
