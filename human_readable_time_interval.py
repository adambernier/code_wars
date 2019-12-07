def output(result):
  if result[1] == 1:
    return '{} {}'.format(result[1], result[0])
  elif result[1] > 1:
    return '{} {}s'.format(result[1], result[0])
  else:
    return None

def divmod_rec(interval, threshold):
  divisor, remainder = divmod(interval, threshold)
  return divisor, remainder

def format_duration(seconds):
  if seconds == 0:
    return 'now'
  
  result = []
  thresholds = [('year',365*24*60*60), ('day',24*60*60), ('hour',60*60), ('minute',60), ('second',0)]
  
  remainder = seconds
  for unit, threshold in thresholds:
    divisor, remainder = divmod_rec(remainder, threshold)
    if divisor > 0:
      result.append((unit, divisor))
    if remainder > 0 and remainder <= 59:
      result.append(('second',remainder))
      break
    elif remainder == 0:
      break 
  
  continue_count = 0
  for item in result:
    continue_count += 1
  
  final = ''
  i = 0
  for res in result:
    if res[1] > 0:
      final += output(res)
      continue_count -= 1

    if i < (len(result)-1):
      if continue_count > 1:
        final += ", "
      else:
        final += " and "
        
    i += 1

  return final
 
