import collections as co 

def factorial(n):
  if n < 2:
    return 1
  else:
    return n * factorial(n-1)

def calc_num_ana(word,proposed_word,frequencies,alpha):
  denom = 1
  fact_remain_alpha = factorial(len(word) - len(proposed_word))
  for freq in frequencies:
    if freq != alpha:
      denom *= factorial(frequencies[freq])
    else:
      denom *= factorial(frequencies[freq] - 1)
  return int(fact_remain_alpha // denom)

def listPosition(word):
  # Return the anagram list position of the word
  # sort the distinct alphabet in ascending order
  # count the frequency of each alphabet  
  frequencies = co.defaultdict(int)
  alpha_arr = []
  
  for i in range(len(word)):
    try:
      idx = alpha_arr.index(word[i])
    except ValueError:
      alpha_arr.append(word[i])
    frequencies[word[i]] += 1
  
  alpha_arr.sort()
  matched_word = ''
  total_anagram = 0
  
  while matched_word != word:
    print(matched_word)
    print(word)
    for a in range(len(alpha_arr)):
      alpha = alpha_arr[a]
      if frequencies[alpha] > 0:
        proposed_word = matched_word + alpha
        idx = word.find(proposed_word)
        if idx == 0:
          # matched; decrement count and update matched word
          frequencies[alpha] -= 1 
          matched_word += alpha
          break
        else:
          # calc num of words needed to be formed
          total_anagram += calc_num_ana(word,proposed_word,frequencies,alpha)
  
  return total_anagram + 1

