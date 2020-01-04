CHAR_COUNT = 256

def get_char_count_list(s): 
    count = [0] * CHAR_COUNT 
    for i in s:
        i = i.lower()
        count[ord(i)] += 1
    return count 

def first_non_repeating_letter(s):
    count = get_char_count_list(s) 
    index = -1
    k = 0
  
    for i in s:
        if count[ord(i.lower())] == 1:
            index = k 
            break
        k += 1
    if index == -1:
        return ''
    else:
        return s[index]
