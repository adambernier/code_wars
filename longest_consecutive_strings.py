def longest_consec(strarr, k):
  longest_len = 0
  longest_str = ''
  iterate_over = []
  if k == 0 or k > len(strarr):
    return ''
  for i in range(k):
    iterate_over.append(strarr[i:])
  try:
    for i in zip(*iterate_over):
      state = ''
      for j in i:
        state += j
      the_len = len(state)
      if the_len > longest_len:
        longest_len = the_len
        longest_str = state
  except IndexError:
    pass
  return longest_str
  
