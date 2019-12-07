def to_weird_case(s):
  s += ' '
  prev = ''
  prev_chg = False
  result = []
  for idx,(c1,c2) in enumerate(zip(s,s[1:])):
    upper = False
    if not prev_chg:
      prev = c1
    else:
      prev = c1.upper()
    if idx == 0:
      if c1 == ' ':
        result.append(c1)
      else:
        result.append(c1.upper())
        upper = False
    if idx > 0 and prev.islower():
      upper = True
    if (upper or prev == ' '):
      result.append(c2.upper())
      prev_chg = True
    else:
      result.append(c2.lower())
      prev_chg = False
  return ''.join(result[:-1])
